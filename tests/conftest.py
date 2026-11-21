"""!
@file conftest.py
@brief Shared test fixtures.
"""

import numpy as np
import pytest

from image_factory import make_image_bytes


@pytest.fixture
def three_colour_pixels() -> np.ndarray:
    """!
    @brief A 10x10 image: 60 red, 30 green and 10 blue pixels.
    @return Array of shape (10, 10, 3).
    """
    pixels = np.zeros((10, 10, 3), dtype=np.uint8)
    pixels[:6] = (255, 0, 0)
    pixels[6:9] = (0, 255, 0)
    pixels[9:] = (0, 0, 255)
    return pixels


@pytest.fixture
def three_colour_png(three_colour_pixels: np.ndarray) -> bytes:
    """!
    @brief The three-colour image as a PNG file.
    @return The PNG bytes.
    """
    return make_image_bytes(three_colour_pixels)
