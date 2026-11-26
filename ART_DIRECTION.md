# Art Direction — The Minute After

## Style

Warm, hand-drawn cartoonist illustrations in the manner of Charlie Mackesy:
loose black ink line drawing on warm cream paper, minimal colour, a touch of
rust orange to match the site accent (`#a44a24`). Quiet, human, tender.
No text inside the illustrations. One illustration per chapter, placed just
under the chapter title, showing that chapter's moment.

## Files

- `assets/cover.png` — portrait book cover. Used as the site cover, the
  preview cover, and the EPUB cover (`pandoc --epub-cover-image`).
- `assets/illustration-<chapter-slug>.png` — e.g.
  `illustration-01-the-pressured-coworker.png`. Wired into the chapter page,
  the preview, and the EPUB automatically by `build.py` when present.

## Prompts

### Cover

Book cover, portrait orientation, for a book titled 'The Minute After' with
subtitle 'Small Acts. Better Days.' and author 'Venkata Sandeep
Dhullipalla'. Warm hand-drawn cartoonist style in the manner of Charlie
Mackesy: loose black ink line drawing on warm cream paper, minimal color
with a touch of rust orange. The drawing shows two simple figures standing
side by side in a large quiet empty room, one slightly behind the other,
soft warm light falling between them. The title 'The Minute After' in large
elegant hand-lettered serif text at the top, the subtitle 'Small Acts.
Better Days.' beneath it, and the author name 'Venkata Sandeep
Dhullipalla' at the bottom. Calm, hopeful, literary.

### Chapter 1 — The Pressured Coworker

Warm hand-drawn cartoonist illustration in the manner of Charlie Mackesy:
loose black ink line drawing on warm cream paper, minimal color. A
conference room, a long table, eight people seated with laptops and coffee
cups. One woman stands at the head of the table presenting, her hand
resting lightly on her laptop. A man at the side leans forward, pen in
hand, mid-interruption. The others look down at their notes. Quiet, human,
tender, no text in the image.

### Chapter 2 — The Helpless Person

Warm hand-drawn cartoonist illustration in the manner of Charlie Mackesy:
loose black ink line drawing on warm cream paper, minimal color. An office
lobby in the morning. A security guard stands calmly behind a small desk,
hands resting on the desk. A man in a suit stands before him, badge in
hand, shoulders raised, mid-shout. A third figure stands quietly beside
the guard, one hand resting lightly on the desk. Soft morning light through
tall windows. Quiet, human, tender, no text in the image.

## Status

- 2026-11-26: generation attempted for the cover and the Chapter 1 and 2
  illustrations; the image service was unavailable (upstream 503, three
  attempts). The prompts above are saved here, and `build.py` is already
  wired to pick the files up the moment they exist. Re-run the generation
  when the service is back, then `python3 build.py`, commit, push.
- Chapters 3-10: write the prompt for each chapter the same way, one image
  per chapter, after the chapter itself is written and approved.
