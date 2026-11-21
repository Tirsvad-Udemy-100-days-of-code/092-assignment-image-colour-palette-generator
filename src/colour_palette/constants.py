"""!
@file constants.py
@brief Every constant of the colour palette generator, defined in one place.
"""

## Number of colours shown in the palette, as the assignment asks.
TOP_COLOUR_COUNT: int = 10

## Width of a colour bucket per channel. Pixels whose channels fall in the
## same bucket count as one colour, so near-identical shades are grouped.
## 1 means exact colours.
DEFAULT_BUCKET_SIZE: int = 24

## Smallest and largest bucket size a user may choose.
MIN_BUCKET_SIZE: int = 1
MAX_BUCKET_SIZE: int = 64

## Longest image side, in pixels, after the image is scaled down for counting.
## Scaling keeps the count fast and the proportions of the colours intact.
MAX_IMAGE_SIDE: int = 300

## Largest accepted upload, in bytes (10 MB).
MAX_UPLOAD_BYTES: int = 10_000_000

## Largest too-large upload that is still read and discarded, so the browser receives the error page
## instead of a reset connection. Anything larger is cut off.
MAX_DISCARD_BYTES: int = 5 * MAX_UPLOAD_BYTES

## Size of the chunks a discarded upload is read in.
DISCARD_CHUNK_BYTES: int = 64 * 1024

## Largest image, in pixels, that is decoded. Guards against decompression bombs.
MAX_IMAGE_PIXELS: int = 50_000_000

## Number of colour channels in an RGB pixel.
RGB_CHANNELS: int = 3

## Number of channels in an RGBA pixel (RGB plus alpha).
RGBA_CHANNELS: int = 4

## Pixels with an alpha value below this are transparent and are not counted.
MIN_VISIBLE_ALPHA: int = 128

## Highest value of one 8-bit colour channel.
MAX_CHANNEL_VALUE: int = 255

## Address and port the web server listens on by default.
DEFAULT_HOST: str = "127.0.0.1"
DEFAULT_PORT: int = 8000

## Name of the form field that carries the uploaded image.
UPLOAD_FIELD_NAME: str = "image"

## Name of the form field that carries the bucket size.
BUCKET_FIELD_NAME: str = "bucket_size"

## Title shown in the browser and on the page.
APP_TITLE: str = "Image Colour Palette Generator"
