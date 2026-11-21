"""!
@file test_html_view.py
@brief Tests of rendering the page.
"""

from colour_palette.domain.colour import ColourShare
from colour_palette.presentation.html_view import image_data_uri, render_page


def test_render_page_without_palette_shows_upload_form() -> None:
    html = render_page()
    assert 'enctype="multipart/form-data"' in html
    assert 'type="file" name="image"' in html
    assert "palette" not in html.split("<main>")[1].split("</form>")[1]


def test_render_page_shows_each_hex_code_and_share() -> None:
    palette = [ColourShare((26, 188, 156), 3, 75.0), ColourShare((44, 62, 80), 1, 25.0)]
    html = render_page(palette=palette)
    assert "#1ABC9C" in html
    assert "#2C3E50" in html
    assert "75.0% of the image" in html


def test_render_page_escapes_error_text() -> None:
    html = render_page(error="<script>alert(1)</script>")
    assert "<script>alert(1)</script>" not in html
    assert "&lt;script&gt;" in html


def test_image_data_uri_embeds_images_only() -> None:
    assert image_data_uri(b"\x89PNG", "image/png") == "data:image/png;base64,iVBORw=="
    assert image_data_uri(b"<svg/>", "image/svg+xml") is None
    assert image_data_uri(b"text", "text/html") is None
