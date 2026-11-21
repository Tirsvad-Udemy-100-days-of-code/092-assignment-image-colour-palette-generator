"""!
@file test_palette_service.py
@brief Tests of the palette use case with a stand-in image reader.
"""

import numpy as np
import pytest

from colour_palette.application.palette_service import PaletteError, PaletteService


class FixedImageReader:
    """!
    @brief Returns the same pixels for any upload and records what it was given.
    """

    def __init__(self, pixels: np.ndarray) -> None:
        self.pixels = pixels
        self.received: bytes | None = None

    def read_pixels(self, image_bytes: bytes) -> np.ndarray:
        self.received = image_bytes
        return self.pixels


def test_build_palette_reads_the_upload_and_counts_its_colours(three_colour_pixels: np.ndarray) -> None:
    reader = FixedImageReader(three_colour_pixels)
    palette = PaletteService(reader).build_palette(b"upload", bucket_size=1)
    assert reader.received == b"upload"
    assert palette[0].hex_code == "#FF0000"


def test_build_palette_passes_count_through(three_colour_pixels: np.ndarray) -> None:
    palette = PaletteService(FixedImageReader(three_colour_pixels)).build_palette(b"x", count=1, bucket_size=1)
    assert len(palette) == 1


def test_build_palette_reports_an_image_without_visible_pixels() -> None:
    transparent = np.zeros((2, 2, 4), dtype=np.uint8)
    with pytest.raises(PaletteError):
        PaletteService(FixedImageReader(transparent)).build_palette(b"x")
