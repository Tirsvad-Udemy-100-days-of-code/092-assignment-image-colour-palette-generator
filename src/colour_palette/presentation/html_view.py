"""!
@file html_view.py
@brief Render the upload page and the palette as HTML.
"""

import base64
from html import escape

from colour_palette.constants import (
    APP_TITLE,
    BUCKET_FIELD_NAME,
    DEFAULT_BUCKET_SIZE,
    MAX_BUCKET_SIZE,
    MIN_BUCKET_SIZE,
    TOP_COLOUR_COUNT,
    UPLOAD_FIELD_NAME,
)
from colour_palette.domain.colour import ColourShare

## Relative luminance above which dark text is used on a swatch.
_LIGHT_SWATCH_LUMINANCE: float = 0.55

_STYLE = """
:root { color-scheme: light dark; --bg: #f5f6fa; --fg: #2f3640; --card: #ffffff; --muted: #718093; --accent: #0097e6; }
@media (prefers-color-scheme: dark) { :root { --bg: #1e272e; --fg: #f5f6fa; --card: #2f3640; --muted: #a4b0be; } }
* { box-sizing: border-box; }
body { margin: 0; font-family: system-ui, sans-serif; background: var(--bg); color: var(--fg); }
main { max-width: 960px; margin: 0 auto; padding: 24px 16px 48px; }
h1 { margin: 0 0 4px; font-size: 1.8rem; }
p.lead { margin: 0 0 24px; color: var(--muted); }
form { background: var(--card); padding: 16px; border-radius: 12px;
  display: flex; flex-wrap: wrap; gap: 12px 24px; align-items: end; }
label { display: flex; flex-direction: column; gap: 6px; font-size: .9rem; color: var(--muted); }
button { background: var(--accent); color: #fff; border: 0; border-radius: 8px;
  padding: 10px 20px; font-size: 1rem; cursor: pointer; }
.error { background: #e84118; color: #fff; padding: 12px 16px; border-radius: 8px; margin-top: 16px; }
.result { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 2fr); gap: 24px; margin-top: 24px; }
@media (max-width: 640px) { .result { grid-template-columns: 1fr; } }
.preview img { width: 100%; border-radius: 12px; }
.palette { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 12px;
  list-style: none; margin: 0; padding: 0; }
.swatch { width: 100%; border-radius: 12px; min-height: 120px; padding: 12px; display: flex; flex-direction: column;
  justify-content: space-between; border: 0; font: inherit; text-align: left; cursor: pointer; }
.swatch .hex { font-size: 1.2rem; font-weight: 700; letter-spacing: .04em; }
.swatch .share { font-size: .85rem; opacity: .85; }
.hint { color: var(--muted); font-size: .85rem; margin-top: 8px; }
"""

_SCRIPT = """
document.querySelectorAll('.swatch').forEach(function (swatch) {
  swatch.addEventListener('click', function () {
    var hex = swatch.dataset.hex;
    var label = swatch.querySelector('.share');
    var original = label.textContent;
    navigator.clipboard.writeText(hex).then(function () {
      label.textContent = 'Copied ' + hex;
      setTimeout(function () { label.textContent = original; }, 1200);
    });
  });
});
"""


def _text_colour_for(colour: ColourShare) -> str:
    """!
    @brief Choose black or white text so the HEX code stays readable on the swatch.
    @param colour The swatch colour.
    @return A CSS colour for the text.
    """
    red, green, blue = colour.rgb
    luminance = (0.299 * red + 0.587 * green + 0.114 * blue) / 255
    return "#2f3640" if luminance > _LIGHT_SWATCH_LUMINANCE else "#ffffff"


def image_data_uri(image_bytes: bytes, content_type: str) -> str | None:
    """!
    @brief Embed an uploaded image in the page so the user sees what was analysed.
    @param image_bytes The raw bytes of the uploaded file.
    @param content_type The content type sent by the browser.
    @return A data URI, or None when the content type is not an image.
    """
    if not content_type.startswith("image/") or "svg" in content_type:
        return None
    encoded = base64.b64encode(image_bytes).decode("ascii")
    return f"data:{content_type};base64,{encoded}"


def _render_palette(palette: list[ColourShare], preview_uri: str | None) -> str:
    """!
    @brief Render the result: the uploaded image beside its colour swatches.
    @param palette The colours, most common first.
    @param preview_uri Data URI of the uploaded image, or None.
    @return HTML for the result section.
    """
    swatches = "\n".join(
        f'<li><button type="button" class="swatch" data-hex="{escape(colour.hex_code)}" '
        f'style="background:{escape(colour.hex_code)};color:{_text_colour_for(colour)}">'
        f'<span class="hex">{escape(colour.hex_code)}</span>'
        f'<span class="share">{colour.percentage:.1f}% of the image</span></button></li>'
        for colour in palette
    )
    preview = (
        f'<div class="preview"><img src="{escape(preview_uri)}" alt="Uploaded image"></div>'
        if preview_uri
        else "<div></div>"
    )
    return (
        f'<section class="result">{preview}<div><ol class="palette">{swatches}</ol>'
        '<p class="hint">Click a colour to copy its HEX code.</p></div></section>'
    )


def render_page(
    palette: list[ColourShare] | None = None,
    error: str | None = None,
    preview_uri: str | None = None,
    bucket_size: int = DEFAULT_BUCKET_SIZE,
) -> str:
    """!
    @brief Render the whole page: the upload form, an error if any, and the palette if any.
    @param palette The colours to show, or None before an upload.
    @param error A message for the user, or None.
    @param preview_uri Data URI of the uploaded image, or None.
    @param bucket_size The bucket size to show in the form.
    @return The HTML document.
    """
    error_html = f'<p class="error" role="alert">{escape(error)}</p>' if error else ""
    result_html = _render_palette(palette, preview_uri) if palette else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(APP_TITLE)}</title>
<style>{_STYLE}</style>
</head>
<body>
<main>
<h1>{escape(APP_TITLE)}</h1>
<p class="lead">Upload an image to see its top {TOP_COLOUR_COUNT} most common colours.</p>
<form method="post" action="/" enctype="multipart/form-data">
<label>Image
<input type="file" name="{UPLOAD_FIELD_NAME}" accept="image/*" required></label>
<label>Colour grouping (1 = exact colours)
<input type="number" name="{BUCKET_FIELD_NAME}" min="{MIN_BUCKET_SIZE}" max="{MAX_BUCKET_SIZE}"
 value="{bucket_size}"></label>
<button type="submit">Find colours</button>
</form>
{error_html}
{result_html}
</main>
<script>{_SCRIPT}</script>
</body>
</html>
"""
