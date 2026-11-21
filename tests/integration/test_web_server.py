"""!
@file test_web_server.py
@brief End-to-end tests of the web server on the loopback interface.
"""

import threading
import urllib.error
import urllib.request
from collections.abc import Iterator

import numpy as np
import pytest

from colour_palette.constants import MAX_UPLOAD_BYTES
from colour_palette.presentation.web_server import create_server
from image_factory import make_image_bytes

# urlopen only reaches the loopback test server, so bandit B310 is marked nosec below.
BOUNDARY = "----palette-integration"


@pytest.fixture
def server_url() -> Iterator[str]:
    """!
    @brief Run the server on a free loopback port for one test.
    """
    server = create_server("127.0.0.1", 0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    host, port = server.server_address[:2]
    yield f"http://{host}:{port}/"
    server.shutdown()
    server.server_close()
    thread.join()


def post_upload(url: str, image_bytes: bytes, bucket_size: str = "1") -> tuple[int, str]:
    """!
    @brief Post an image like the browser form does.
    @return The status and the HTML of the response.
    """
    body = (
        (
            f'--{BOUNDARY}\r\nContent-Disposition: form-data; name="image"; filename="test.png"\r\n'
            "Content-Type: image/png\r\n\r\n"
        ).encode()
        + image_bytes
        + (
            f'\r\n--{BOUNDARY}\r\nContent-Disposition: form-data; name="bucket_size"\r\n\r\n{bucket_size}\r\n'
            f"--{BOUNDARY}--\r\n"
        ).encode()
    )
    request = urllib.request.Request(
        url, data=body, headers={"Content-Type": f"multipart/form-data; boundary={BOUNDARY}"}, method="POST"
    )
    try:
        with urllib.request.urlopen(request, timeout=10) as response:  # nosec B310
            return response.status, response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        return error.code, error.read().decode("utf-8")


def test_get_shows_upload_form(server_url: str) -> None:
    with urllib.request.urlopen(server_url, timeout=10) as response:  # nosec B310
        assert response.status == 200
        assert 'type="file"' in response.read().decode("utf-8")


def test_unknown_path_returns_not_found(server_url: str) -> None:
    with pytest.raises(urllib.error.HTTPError) as caught:
        urllib.request.urlopen(server_url + "missing", timeout=10)  # nosec B310
    assert caught.value.code == 404


def test_upload_shows_top_colours(server_url: str, three_colour_png: bytes) -> None:
    status, html = post_upload(server_url, three_colour_png)
    assert status == 200
    assert html.index("#FF0000") < html.index("#00FF00") < html.index("#0000FF")
    assert "60.0% of the image" in html


def test_upload_of_many_colours_shows_ten(server_url: str) -> None:
    pixels = np.random.default_rng(seed=92).integers(0, 256, size=(40, 40, 3), dtype=np.uint8)
    status, html = post_upload(server_url, make_image_bytes(pixels))
    assert status == 200
    assert html.count('class="swatch"') == 10


def test_upload_of_non_image_shows_error(server_url: str) -> None:
    status, html = post_upload(server_url, b"not an image")
    assert status == 400
    assert "not an image" in html


def test_upload_without_file_shows_error(server_url: str) -> None:
    status, html = post_upload(server_url, b"")
    assert status == 400
    assert "Please choose an image" in html


def test_upload_over_the_limit_is_refused(server_url: str) -> None:
    status, html = post_upload(server_url, b"0" * (MAX_UPLOAD_BYTES + 1))
    assert status == 413
    assert "too large" in html


def test_fully_transparent_image_shows_error(server_url: str) -> None:
    status, html = post_upload(server_url, make_image_bytes(np.zeros((4, 4, 4)), mode="RGBA"))
    assert status == 400
    assert "no visible pixels" in html
