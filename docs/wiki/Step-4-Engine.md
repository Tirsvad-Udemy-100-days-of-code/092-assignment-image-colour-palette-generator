# Step 4: Engine

🌐 **English** · [Dansk](Step-4-Engine-da) · [Bahasa Melayu](Step-4-Engine-ms)

Milestone `MIL-004`. Branch and pull request: one for this step.

![36 engine tests passing with 100 % coverage](https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/092-assignment-image-colour-palette-generator/raw/branch/main/docs/images/04-engine-tests.png)

## What was done

The colour counting, with no web page yet. `PillowImageReader` decodes the
upload, converts it to RGBA and scales it so the longer side is at most 300 px.
`find_top_colours` drops transparent pixels, groups the shades and returns the
ten most common colours as `ColourShare` values with a HEX code and a share in
percent. `PaletteService` ties the two together. The unit tests build their
images in memory.

## What was gained

- An image is just an array. Pillow decodes it, and `reshape(-1, 4)` turns a
  `(height, width, 4)` array into a list of pixels (Day 76 knowledge put to
  use).
- A boolean mask removes transparent pixels in one line:
  `pixels[pixels[:, 3] >= MIN_VISIBLE_ALPHA, :3]`.
- `np.unique(pixels, axis=0, return_counts=True)` counts every distinct colour
  in one call, and `np.argsort(-counts)[:10]` picks the ten most common. No
  Python loop over pixels is needed.
- A photo has thousands of almost identical shades. Grouping each channel into
  buckets 24 wide (`DEFAULT_BUCKET_SIZE`, 1 to 64 allowed) makes them count as
  one colour, so the top 10 shows real colours instead of ten shades of the sky.
- Scaling down to 300 px keeps the proportions of the colours and makes
  counting fast.
- A HEX code is just the three channels written in base 16:
  `f"#{red:02X}{green:02X}{blue:02X}"`.
- Keeping NumPy in the domain and Pillow in infrastructure means the counting is
  tested with plain arrays, without image files.
