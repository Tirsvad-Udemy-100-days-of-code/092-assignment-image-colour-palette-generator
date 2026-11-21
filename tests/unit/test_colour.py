"""!
@file test_colour.py
@brief Tests of the colour value objects.
"""

import pytest

from colour_palette.domain.colour import ColourShare, rgb_to_hex


def test_rgb_to_hex_formats_upper_case_with_hash() -> None:
    assert rgb_to_hex(26, 188, 156) == "#1ABC9C"


def test_rgb_to_hex_pads_single_digits() -> None:
    assert rgb_to_hex(0, 5, 15) == "#00050F"


@pytest.mark.parametrize("channels", [(-1, 0, 0), (0, 256, 0), (0, 0, 300)])
def test_rgb_to_hex_rejects_out_of_range_channels(channels: tuple[int, int, int]) -> None:
    with pytest.raises(ValueError):
        rgb_to_hex(*channels)


def test_colour_share_exposes_hex_code() -> None:
    share = ColourShare(rgb=(255, 255, 255), pixel_count=4, percentage=100.0)
    assert share.hex_code == "#FFFFFF"
