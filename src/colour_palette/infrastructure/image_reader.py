"""!
@file image_reader.py
@brief Decode uploaded image files with Pillow.
"""

import io

import numpy as np
from numpy.typing import NDArray
from PIL import Image, UnidentifiedImageError

from colour_palette.constants import MAX_IMAGE_PIXELS, MAX_IMAGE_SIDE


class InvalidImageError(ValueError):
    """!
    @brief Raised when an uploaded file cannot be read as an image.
    """


class PillowImageReader:
    """!
    @brief Reads PNG, JPEG, GIF, BMP, WebP and other Pillow formats into RGB pixels.
    """

    def __init__(self, max_side: int = MAX_IMAGE_SIDE) -> None:
        """!
        @brief Create the reader.
        @param max_side Longest side, in pixels, the image is scaled down to before counting.
        """
        self._max_side = max_side

    def read_pixels(self, image_bytes: bytes) -> NDArray[np.uint8]:
        """!
        @brief Decode an image file and scale it down.
        @param image_bytes The raw bytes of the uploaded file.
        @return Array of shape (height, width, 4) with RGBA values; the domain drops transparent pixels.
        @throws InvalidImageError When the bytes are empty, not an image, or the image is too large.
        """
        if not image_bytes:
            raise InvalidImageError("No file was uploaded")
        Image.MAX_IMAGE_PIXELS = MAX_IMAGE_PIXELS
        try:
            with Image.open(io.BytesIO(image_bytes)) as image:
                image.draft("RGB", (self._max_side, self._max_side))
                rgba_image = image.convert("RGBA")
                rgba_image.thumbnail((self._max_side, self._max_side))
                return np.asarray(rgba_image, dtype=np.uint8)
        except (UnidentifiedImageError, Image.DecompressionBombError, OSError) as error:
            raise InvalidImageError("The file is not an image that can be read") from error
