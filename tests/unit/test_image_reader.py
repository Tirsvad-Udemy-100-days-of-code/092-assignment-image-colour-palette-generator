"""!
@file test_image_reader.py
@brief Tests of decoding uploaded images with Pillow.
"""

import numpy as np
import pytest

from colour_palette.infrastructure.image_reader import InvalidImageError, PillowImageReader
from image_factory import make_image_bytes


def test_read_pixels_returns_rgb_array(three_colour_png: bytes) -> None:
    pixels = PillowImageReader().read_pixels(three_colour_png)
    assert pixels.shape == (10, 10, 4)
    assert pixels.dtype == np.uint8
    assert tuple(pixels[0, 0]) == (255, 0, 0, 255)


def test_read_pixels_scales_down_large_images() -> None:
    large = np.full((400, 800, 3), 128, dtype=np.uint8)
    pixels = PillowImageReader(max_side=100).read_pixels(make_image_bytes(large))
    assert max(pixels.shape[:2]) == 100


def test_read_pixels_reads_jpeg() -> None:
    blue = np.full((16, 16, 3), (0, 0, 255), dtype=np.uint8)
    pixels = PillowImageReader().read_pixels(make_image_bytes(blue, image_format="JPEG"))
    assert pixels.shape == (16, 16, 4)


def test_read_pixels_keeps_the_alpha_channel() -> None:
    transparent = np.zeros((4, 4, 4), dtype=np.uint8)
    pixels = PillowImageReader().read_pixels(make_image_bytes(transparent, mode="RGBA"))
    assert pixels[0, 0, 3] == 0


def test_read_pixels_rejects_empty_upload() -> None:
    with pytest.raises(InvalidImageError):
        PillowImageReader().read_pixels(b"")


def test_read_pixels_rejects_non_image_bytes() -> None:
    with pytest.raises(InvalidImageError):
        PillowImageReader().read_pixels(b"this is not an image")
