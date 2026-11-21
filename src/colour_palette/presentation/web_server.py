"""!
@file web_server.py
@brief A small web server, built on the standard library, that shows the palette of an uploaded image.
"""

import logging
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from colour_palette.application.palette_service import PaletteError, PaletteService
from colour_palette.constants import (
    BUCKET_FIELD_NAME,
    DEFAULT_BUCKET_SIZE,
    DISCARD_CHUNK_BYTES,
    MAX_BUCKET_SIZE,
    MAX_DISCARD_BYTES,
    MAX_UPLOAD_BYTES,
    MIN_BUCKET_SIZE,
    UPLOAD_FIELD_NAME,
)
from colour_palette.infrastructure.image_reader import InvalidImageError, PillowImageReader
from colour_palette.presentation.html_view import image_data_uri, render_page
from colour_palette.presentation.multipart_form import FormField, FormParseError, parse_multipart_form

logger = logging.getLogger(__name__)


def read_bucket_size(fields: dict[str, FormField]) -> int:
    """!
    @brief Read the bucket size from the form, falling back to the default.
    @param fields The submitted form fields.
    @return A bucket size within the allowed range.
    """
    field = fields.get(BUCKET_FIELD_NAME)
    if field is None:
        return DEFAULT_BUCKET_SIZE
    try:
        value = int(field.data.decode("ascii").strip())
    except UnicodeDecodeError, ValueError:
        return DEFAULT_BUCKET_SIZE
    return max(MIN_BUCKET_SIZE, min(MAX_BUCKET_SIZE, value))


class PaletteRequestHandler(BaseHTTPRequestHandler):
    """!
    @brief Serves the upload page (GET /) and the palette (POST /).
    """

    ## The use case the handler calls; set by create_server.
    palette_service: PaletteService = PaletteService(PillowImageReader())

    def do_GET(self) -> None:  # noqa: N802 (name set by BaseHTTPRequestHandler)
        """!
        @brief Show the upload page.
        """
        if self.path.split("?", 1)[0] != "/":
            self._send_html(HTTPStatus.NOT_FOUND, render_page(error="Page not found."))
            return
        self._send_html(HTTPStatus.OK, render_page())

    def do_POST(self) -> None:  # noqa: N802 (name set by BaseHTTPRequestHandler)
        """!
        @brief Read the uploaded image and show its palette.
        """
        if self.path.split("?", 1)[0] != "/":
            self._send_html(HTTPStatus.NOT_FOUND, render_page(error="Page not found."))
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            length = -1
        if length <= 0:
            self._send_html(HTTPStatus.BAD_REQUEST, render_page(error="Please choose an image to upload."))
            return
        if length > MAX_UPLOAD_BYTES:
            self._discard_body(length)
            self.close_connection = True
            limit_mb = MAX_UPLOAD_BYTES // 1_000_000
            self._send_html(
                HTTPStatus.REQUEST_ENTITY_TOO_LARGE,
                render_page(error=f"The image is too large. The limit is {limit_mb} MB."),
            )
            return

        body = self.rfile.read(length)
        try:
            fields = parse_multipart_form(body, self.headers.get("Content-Type", ""))
        except FormParseError as error:
            self._send_html(HTTPStatus.BAD_REQUEST, render_page(error=str(error)))
            return

        bucket_size = read_bucket_size(fields)
        upload = fields.get(UPLOAD_FIELD_NAME)
        if upload is None or not upload.data:
            self._send_html(
                HTTPStatus.BAD_REQUEST,
                render_page(error="Please choose an image to upload.", bucket_size=bucket_size),
            )
            return
        try:
            palette = self.palette_service.build_palette(upload.data, bucket_size=bucket_size)
        except (InvalidImageError, PaletteError) as error:
            self._send_html(HTTPStatus.BAD_REQUEST, render_page(error=str(error), bucket_size=bucket_size))
            return

        preview = image_data_uri(upload.data, upload.content_type)
        self._send_html(HTTPStatus.OK, render_page(palette=palette, preview_uri=preview, bucket_size=bucket_size))

    def log_message(self, message_format: str, *args: object) -> None:
        """!
        @brief Send request logs to the logging module instead of stderr.
        @param message_format The printf-style format from the base class.
        @param args The values for the format.
        """
        logger.info("%s - %s", self.address_string(), message_format % args)

    def _discard_body(self, length: int) -> None:
        """!
        @brief Read and drop a refused upload, up to MAX_DISCARD_BYTES, so the client can read the reply.
        @param length The Content-Length of the request.
        """
        remaining = min(length, MAX_DISCARD_BYTES)
        while remaining > 0:
            chunk = self.rfile.read(min(DISCARD_CHUNK_BYTES, remaining))
            if not chunk:
                break
            remaining -= len(chunk)

    def _send_html(self, status: HTTPStatus, html: str) -> None:
        """!
        @brief Send an HTML response.
        @param status The HTTP status.
        @param html The HTML document.
        """
        payload = html.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header(
            "Content-Security-Policy",
            "default-src 'none'; img-src data:; style-src 'unsafe-inline'; "
            "script-src 'unsafe-inline'; form-action 'self'",
        )
        self.end_headers()
        self.wfile.write(payload)


def create_server(host: str, port: int, palette_service: PaletteService | None = None) -> ThreadingHTTPServer:
    """!
    @brief Create the web server without starting it.
    @param host Address to listen on.
    @param port Port to listen on; 0 picks a free port.
    @param palette_service The use case to serve; the default reads images with Pillow.
    @return The server, ready for serve_forever().
    """
    service = palette_service or PaletteService(PillowImageReader())
    handler = type("ConfiguredPaletteRequestHandler", (PaletteRequestHandler,), {"palette_service": service})
    return ThreadingHTTPServer((host, port), handler)
