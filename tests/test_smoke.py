"""!
@file test_smoke.py
@brief Smoke test: the package imports and its constants follow the assignment.
"""

import colour_palette
from colour_palette import constants


def test_package_has_a_version() -> None:
    assert colour_palette.__version__ == "0.1.0"


def test_palette_shows_ten_colours() -> None:
    assert constants.TOP_COLOUR_COUNT == 10


def test_default_bucket_size_is_within_the_allowed_range() -> None:
    assert constants.MIN_BUCKET_SIZE <= constants.DEFAULT_BUCKET_SIZE <= constants.MAX_BUCKET_SIZE
