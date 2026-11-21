"""!
@file palette_service.py
@brief The use case "Show the top colours of an uploaded image".
"""

from typing import Protocol

import numpy as np
from numpy.typing import NDArray

from colour_palette.constants import DEFAULT_BUCKET_SIZE, TOP_COLOUR_COUNT
from colour_palette.domain.colour import ColourShare
from colour_palette.domain.palette import find_top_colours


class PaletteError(ValueError):
    """!
    @brief Raised when an image has nothing that can be counted, for example only transparent pixels.
    """


class ImageReader(Protocol):
    """!
    @brief Turns the bytes of an image file into RGB pixels.
    """

    def read_pixels(self, image_bytes: bytes) -> NDArray[np.uint8]:
        """!
        @brief Decode an image file.
        @param image_bytes The raw bytes of the uploaded file.
        @return Array of shape (height, width, 3 or 4) with RGB or RGBA values.
        """
        ...


class PaletteService:
    """!
    @brief Builds the colour palette of an uploaded image.
    """

    def __init__(self, image_reader: ImageReader) -> None:
        """!
        @brief Create the service.
        @param image_reader Decodes the uploaded files.
        """
        self._image_reader = image_reader

    def build_palette(
        self,
        image_bytes: bytes,
        count: int = TOP_COLOUR_COUNT,
        bucket_size: int = DEFAULT_BUCKET_SIZE,
    ) -> list[ColourShare]:
        """!
        @brief Find the most common colours of an uploaded image.
        @param image_bytes The raw bytes of the uploaded file.
        @param count Number of colours to return.
        @param bucket_size Width of a colour bucket per channel.
        @return The colours, most common first.
        """
        pixels = self._image_reader.read_pixels(image_bytes)
        try:
            return find_top_colours(pixels, count=count, bucket_size=bucket_size)
        except ValueError as error:
            raise PaletteError(str(error)) from error
