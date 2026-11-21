"""!
@file test_palette.py
@brief Tests of finding the most common colours with NumPy.
"""

import numpy as np
import pytest

from colour_palette.domain.palette import find_top_colours, quantise_pixels


def test_find_top_colours_orders_by_frequency(three_colour_pixels: np.ndarray) -> None:
    palette = find_top_colours(three_colour_pixels, bucket_size=1)
    assert [colour.hex_code for colour in palette] == ["#FF0000", "#00FF00", "#0000FF"]
    assert [colour.pixel_count for colour in palette] == [60, 30, 10]


def test_find_top_colours_reports_percentages(three_colour_pixels: np.ndarray) -> None:
    palette = find_top_colours(three_colour_pixels, bucket_size=1)
    assert [round(colour.percentage, 1) for colour in palette] == [60.0, 30.0, 10.0]


def test_find_top_colours_returns_at_most_ten_by_default() -> None:
    random_pixels = np.random.default_rng(seed=92).integers(0, 256, size=(50, 50, 3), dtype=np.uint8)
    palette = find_top_colours(random_pixels, bucket_size=1)
    assert len(palette) == 10
    counts = [colour.pixel_count for colour in palette]
    assert counts == sorted(counts, reverse=True)


def test_find_top_colours_returns_fewer_when_image_has_fewer_colours(three_colour_pixels: np.ndarray) -> None:
    assert len(find_top_colours(three_colour_pixels, count=10, bucket_size=1)) == 3


def test_find_top_colours_respects_count(three_colour_pixels: np.ndarray) -> None:
    palette = find_top_colours(three_colour_pixels, count=2, bucket_size=1)
    assert [colour.hex_code for colour in palette] == ["#FF0000", "#00FF00"]


def test_find_top_colours_accepts_flat_pixel_list() -> None:
    pixels = np.array([[10, 20, 30], [10, 20, 30], [1, 2, 3]], dtype=np.uint8)
    palette = find_top_colours(pixels, bucket_size=1)
    assert palette[0].hex_code == "#0A141E"
    assert palette[0].pixel_count == 2


def test_bucketing_groups_near_identical_shades() -> None:
    pixels = np.array([[200, 10, 10], [205, 12, 9], [0, 0, 0]], dtype=np.uint8)
    palette = find_top_colours(pixels, bucket_size=24)
    assert palette[0].pixel_count == 2


def test_quantise_pixels_centres_each_channel_in_its_bucket() -> None:
    pixels = np.array([[0, 23, 24]], dtype=np.uint8)
    assert quantise_pixels(pixels, 24).tolist() == [[12, 12, 36]]


def test_quantise_pixels_never_exceeds_channel_maximum() -> None:
    pixels = np.array([[255, 255, 255]], dtype=np.uint8)
    assert quantise_pixels(pixels, 60).tolist() == [[255, 255, 255]]


def test_quantise_pixels_with_bucket_size_one_keeps_exact_colours() -> None:
    pixels = np.array([[1, 2, 3]], dtype=np.uint8)
    assert quantise_pixels(pixels, 1).tolist() == [[1, 2, 3]]


@pytest.mark.parametrize("bucket_size", [0, 65])
def test_quantise_pixels_rejects_bucket_size_out_of_range(bucket_size: int) -> None:
    with pytest.raises(ValueError):
        quantise_pixels(np.zeros((1, 3), dtype=np.uint8), bucket_size)


def test_find_top_colours_ignores_transparent_pixels() -> None:
    pixels = np.array([[0, 0, 0, 0], [0, 0, 0, 127], [9, 9, 9, 128], [9, 9, 9, 255]], dtype=np.uint8)
    palette = find_top_colours(pixels, bucket_size=1)
    assert [(colour.hex_code, colour.pixel_count) for colour in palette] == [("#090909", 2)]
    assert palette[0].percentage == 100.0


def test_find_top_colours_rejects_fully_transparent_image() -> None:
    with pytest.raises(ValueError):
        find_top_colours(np.zeros((4, 4, 4), dtype=np.uint8))


def test_find_top_colours_rejects_non_rgb_array() -> None:
    with pytest.raises(ValueError):
        find_top_colours(np.zeros((4, 4, 2), dtype=np.uint8))


def test_find_top_colours_returns_one_colour_for_a_plain_image() -> None:
    palette = find_top_colours(np.full((5, 5, 3), 77, dtype=np.uint8), bucket_size=1)
    assert len(palette) == 1
    assert palette[0].percentage == 100.0


def test_find_top_colours_rejects_empty_image() -> None:
    with pytest.raises(ValueError):
        find_top_colours(np.zeros((0, 3), dtype=np.uint8))


def test_find_top_colours_rejects_count_below_one(three_colour_pixels: np.ndarray) -> None:
    with pytest.raises(ValueError):
        find_top_colours(three_colour_pixels, count=0)
