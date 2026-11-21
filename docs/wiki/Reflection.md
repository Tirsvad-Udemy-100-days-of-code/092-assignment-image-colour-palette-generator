# Reflection

🌐 **English** · [Dansk](Reflection-da) · [Bahasa Melayu](Reflection-ms)

## How I approached the project

I planned before coding: a Business Case, a Stakeholder Analysis and six
milestones, each with its own branch and pull request. The design (use case,
ADRs and diagrams) came before the engine, and the engine came before the
website, so each step stood on a tested one.

## What was easy

- Counting colours with NumPy. Once the image is an array,
  `np.unique(axis=0, return_counts=True)` and `np.argsort` do the whole job in
  two lines.
- Converting RGB to HEX with an f-string.
- Testing the engine: images built in memory with known colours give exact
  expected results.

## What was hard

- Getting colours that look right. Counting exact colours in a photo gives ten
  shades of the same sky, so the shades had to be grouped, and the bucket size
  is a trade-off between detail and a useful palette.
- Reading the upload without a web framework. The `cgi` module is gone in
  Python 3.13, so the multipart form is parsed with `email.parser`.
- Transparent images, which are easy to forget until the use case asks about
  them.

## What I would do differently next time

- Decide the screenshot for each step while planning, so it is taken when the
  step is merged and not afterwards.
- Write the alternative flows of the use case even earlier. They found most of
  the error cases the website later had to handle.

## Biggest learning

An image is just a NumPy array, and most image questions are array questions.
The hard part is not the counting but deciding what "the same colour" means.
