"""!
@file test_multipart_form.py
@brief Tests of reading multipart form uploads.
"""

import pytest

from colour_palette.presentation.multipart_form import FormParseError, parse_multipart_form

BOUNDARY = "----palette-test"


def build_body(*parts: tuple[str, bytes, str | None]) -> bytes:
    """!
    @brief Build a multipart body from (name, data, filename) parts.
    """
    chunks = []
    for name, data, filename in parts:
        disposition = f'form-data; name="{name}"'
        headers = f"Content-Disposition: {disposition}"
        if filename:
            headers += f'; filename="{filename}"\r\nContent-Type: image/png'
        chunks.append(f"--{BOUNDARY}\r\n{headers}\r\n\r\n".encode() + data + b"\r\n")
    return b"".join(chunks) + f"--{BOUNDARY}--\r\n".encode()


def test_parse_multipart_form_reads_file_and_text_fields() -> None:
    binary = bytes(range(256))
    body = build_body(("image", binary, "photo.png"), ("bucket_size", b"8", None))
    fields = parse_multipart_form(body, f"multipart/form-data; boundary={BOUNDARY}")
    assert fields["image"].data == binary
    assert fields["image"].filename == "photo.png"
    assert fields["image"].content_type == "image/png"
    assert fields["bucket_size"].data == b"8"


def test_parse_multipart_form_rejects_other_content_types() -> None:
    with pytest.raises(FormParseError):
        parse_multipart_form(b"a=1", "application/x-www-form-urlencoded")
