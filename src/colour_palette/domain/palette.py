"""!
@file palette.py
@brief Find the most common colours in an array of pixels with NumPy.
"""

import numpy as np
from numpy.typing import NDArray

from colour_palette.constants import (
    DEFAULT_BUCKET_SIZE,
    MAX_BUCKET_SIZE,
    MAX_CHANNEL_VALUE,
    MIN_BUCKET_SIZE,
    MIN_VISIBLE_ALPHA,
    RGB_CHANNELS,
    RGBA_CHANNELS,
    TOP_COLOUR_COUNT,
)
from colour_palette.domain.colour import ColourShare


def quantise_pixels(pixels: NDArray[np.uint8], bucket_size: int) -> NDArray[np.uint8]:
    """!
    @brief Move every channel to the middle of its bucket, so similar shades become one colour.
    @param pixels Array of shape (N, 3) with RGB values.
    @param bucket_size Width of a bucket per channel; 1 keeps the exact colours.
    @return Array of the same shape with the grouped colours.
    @throws ValueError When the bucket size is outside the allowed range.
    """
    if not MIN_BUCKET_SIZE <= bucket_size <= MAX_BUCKET_SIZE:
        raise ValueError(f"Bucket size must be {MIN_BUCKET_SIZE} to {MAX_BUCKET_SIZE}, got {bucket_size}")
    if bucket_size == 1:
        return pixels
    wide = pixels.astype(np.uint16)
    centred = (wide // bucket_size) * bucket_size + bucket_size // 2
    return np.minimum(centred, MAX_CHANNEL_VALUE).astype(np.uint8)


def find_top_colours(
    image: NDArray[np.uint8],
    count: int = TOP_COLOUR_COUNT,
    bucket_size: int = DEFAULT_BUCKET_SIZE,
) -> list[ColourShare]:
    """!
    @brief Find the most common colours in an RGB or RGBA image.
    @param image Array of shape (height, width, 3 or 4) or (N, 3 or 4); with 4 channels,
           pixels with alpha below MIN_VISIBLE_ALPHA are not counted.
    @param count Number of colours to return.
    @param bucket_size Width of a colour bucket per channel; 1 counts exact colours.
    @return The colours, most common first; fewer than count when the image has fewer colours.
    @throws ValueError When the array is not RGB or RGBA, has no visible pixels, or count is below 1.
    """
    if count < 1:
        raise ValueError(f"Count must be at least 1, got {count}")
    channels = image.shape[-1] if image.ndim in (2, 3) else 0
    if channels not in (RGB_CHANNELS, RGBA_CHANNELS):
        raise ValueError(f"Expected RGB or RGBA pixels, got shape {image.shape}")
    pixels = image.reshape(-1, channels)
    if channels == RGBA_CHANNELS:
        pixels = pixels[pixels[:, 3] >= MIN_VISIBLE_ALPHA, :RGB_CHANNELS]
    if pixels.shape[0] == 0:
        raise ValueError("The image has no visible pixels")

    grouped = quantise_pixels(pixels, bucket_size)
    colours, counts = np.unique(grouped, axis=0, return_counts=True)
    # Stable sort on the negated counts: most common first, ties keep colour order.
    order = np.argsort(-counts, kind="stable")[:count]
    total = int(pixels.shape[0])
    return [
        ColourShare(
            rgb=(int(colours[index][0]), int(colours[index][1]), int(colours[index][2])),
            pixel_count=int(counts[index]),
            percentage=float(counts[index]) * 100.0 / total,
        )
        for index in order
    ]
