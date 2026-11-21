"""!
@file colour.py
@brief The colour value objects of the domain.
"""

from dataclasses import dataclass

from colour_palette.constants import MAX_CHANNEL_VALUE


def rgb_to_hex(red: int, green: int, blue: int) -> str:
    """!
    @brief Format an RGB colour as a HEX code.
    @param red Red channel, 0 to 255.
    @param green Green channel, 0 to 255.
    @param blue Blue channel, 0 to 255.
    @return The HEX code in upper case, for example "#1ABC9C".
    @throws ValueError When a channel is outside 0 to 255.
    """
    for channel in (red, green, blue):
        if not 0 <= channel <= MAX_CHANNEL_VALUE:
            raise ValueError(f"Channel value {channel} is outside 0 to {MAX_CHANNEL_VALUE}")
    return f"#{red:02X}{green:02X}{blue:02X}"


@dataclass(frozen=True)
class ColourShare:
    """!
    @brief One colour of the palette and how much of the image it covers.
    """

    ## Red, green and blue channels, 0 to 255.
    rgb: tuple[int, int, int]
    ## Number of counted pixels with this colour.
    pixel_count: int
    ## Share of the counted pixels, 0.0 to 100.0.
    percentage: float

    @property
    def hex_code(self) -> str:
        """!
        @brief The colour as a HEX code.
        @return The HEX code, for example "#1ABC9C".
        """
        return rgb_to_hex(*self.rgb)
