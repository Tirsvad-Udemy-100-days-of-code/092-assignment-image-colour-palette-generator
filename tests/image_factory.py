"""!
@file image_factory.py
@brief Build image files in memory, so no test reads files from disk.
"""

import io

import numpy as np
from PIL import Image


def make_image_bytes(pixels: np.ndarray, image_format: str = "PNG", mode: str = "RGB") -> bytes:
    """!
    @brief Encode an array of pixels as an image file in memory.
    @param pixels Array of shape (height, width, channels).
    @param image_format Pillow format name.
    @param mode Pillow image mode.
    @return The encoded file.
    """
    buffer = io.BytesIO()
    Image.fromarray(pixels.astype(np.uint8), mode=mode).save(buffer, format=image_format)
    return buffer.getvalue()
