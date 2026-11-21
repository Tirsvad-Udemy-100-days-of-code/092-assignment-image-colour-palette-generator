# Step 5: Website

🌐 **English** · [Dansk](Step-5-Website-da) · [Bahasa Melayu](Step-5-Website-ms)

Milestone `MIL-005`. Branch and pull request: one for this step.

![Upload page](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/092-assignment-image-colour-palette-generator/raw/branch/main/docs/images/05-website-upload-form.png)

![Top 10 colours of the sample image](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/092-assignment-image-colour-palette-generator/raw/branch/main/docs/images/05-website-top-ten-colours.png)

## What was done

A page with a file field, a *Colour grouping* field and a **Find colours**
button, served by `http.server` from the standard library. After the upload the
page shows the image beside ten swatches, most common first, each with its HEX
code and its share of the image. Clicking a swatch copies the HEX code. The
upload is read in memory and never stored.

## What was gained

- How a browser sends a file: `multipart/form-data`. The `cgi` module that
  used to parse it was removed in Python 3.13, so the form is parsed with
  `email.parser.BytesParser` instead.
- A website does not need a web framework. Keeping the server on the standard
  library leaves NumPy and Pillow as the only runtime dependencies.
- Limits belong in `constants.py`: the upload is capped at 10 MB
  (`MAX_UPLOAD_BYTES`) and the image at 50 million pixels
  (`MAX_IMAGE_PIXELS`), so one large upload cannot stop the server.
- Web tests can run the real server on `127.0.0.1` and a free port, so the
  whole flow is tested without a browser.
