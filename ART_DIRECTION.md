# Art Direction — The Minute After

## Style

Warm, hand-drawn cartoonist illustrations in the manner of Charlie Mackesy:
loose black ink line drawing on warm cream paper, minimal colour, a touch of
rust orange to match the site accent (`#a44a24`). Quiet, human, tender.
No text inside the illustrations. One illustration per chapter, placed just
under the chapter title, showing that chapter's moment.

## Files

- `assets/cover.jpg` — portrait book cover, 1600x2560 (KDP-ideal). JPEG to
  keep the EPUB small (KDP charges delivery by size). The typographic cover
  is kept as a backup at `assets/cover-typographic.png`. Used as the site
  cover, the preview cover, and the EPUB cover (`pandoc --epub-cover-image`).
- `assets/illustration-<chapter-slug>.jpg` — e.g.
  `illustration-01-the-pressured-coworker.jpg`. JPEG quality 88, landscape
  1920x1280. Wired into the chapter page, the preview, and the EPUB
  automatically by `build.py` when present.

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

### Chapter 3 — The Meeting Where Nobody Speaks

Warm hand-drawn cartoonist illustration in the manner of Charlie Mackesy:
loose black ink line drawing on warm cream paper, minimal color. A
conference room, a man at a whiteboard with a marker, dates underlined
twice, ten people seated around a long table looking down at their notes,
one person raising a hand to ask a question. Quiet tension, no text in the
image.

### Chapter 4 — The New Joiner Nobody Helps

Warm hand-drawn cartoonist illustration in the manner of Charlie Mackesy:
loose black ink line drawing on warm cream paper, minimal color. A young
woman sits alone at a desk in a busy open office, eating a sandwich
one-handed while reading a document on her phone, a laptop open beside
her; around her, colleagues work at their desks, nobody looking her way.
Quiet, human, tender, no text in the image.

### Chapter 5 — The Angry Customer

Warm hand-drawn cartoonist illustration in the manner of Charlie Mackesy:
loose black ink line drawing on warm cream paper, minimal color. A young
woman at a desk in an open office, wearing a headset, listening to a phone
on speaker, her hands folded tightly in her lap; a colleague pulls up a
chair and sits beside her, leaning in calmly. Quiet, human, tender, no
text in the image.

### Chapter 6 — The Blame That Lands on the Wrong Person

Warm hand-drawn cartoonist illustration in the manner of Charlie Mackesy:
loose black ink line drawing on warm cream paper, minimal color. A meeting
room, a woman sits with her hands folded on the table in front of her
notes while a man across the table asks her a question; beside her, a
colleague leans forward, about to speak. Quiet, human, tender, no text in
the image.

### Chapter 7 — The Sharp Reply at Home

Warm hand-drawn cartoonist illustration in the manner of Charlie Mackesy:
loose black ink line drawing on warm cream paper, minimal color. A hallway
at home in the evening, warm lamplight, a man with a bag still on his
shoulder standing in a doorway, a woman in the kitchen turning toward him,
a small child peeking from behind a doorframe holding a drawing. Quiet,
human, tender, no text in the image.

### Chapter 8 — The Stranger in the Queue

Warm hand-drawn cartoonist illustration in the manner of Charlie Mackesy:
loose black ink line drawing on warm cream paper, minimal color. A grocery
store checkout, an old woman counting coins from a small purse on the
counter, a cashier waiting patiently, a queue of people behind her, a man
stepping forward with a few coins in his hand. Quiet, human, tender, no
text in the image.

### Chapter 9 — The Burnt-Out Friend

Warm hand-drawn cartoonist illustration in the manner of Charlie Mackesy:
loose black ink line drawing on warm cream paper, minimal color. An office
late in the evening, a man at a desk with three monitors and a cold cup of
coffee, rubbing the back of his neck, his jacket hanging over his chair; a
colleague stands quietly beside his desk. Quiet, human, tender, no text in
the image.

### Chapter 10 — The Day You Were the Difficult One

Warm hand-drawn cartoonist illustration in the manner of Charlie Mackesy:
loose black ink line drawing on warm cream paper, minimal color. A
boardroom, a woman presenting an idea at the head of the table, a man
beside her stopping mid-sentence, his hand raised, turning toward her;
directors listening around the table. Quiet, human, tender, no text in the
image.

## Status

- 2026-11-26: generation attempted for the cover and the Chapter 1 and 2
  illustrations; the image service was unavailable (upstream 503, three
  attempts). The prompts above are saved here, and `build.py` is already
  wired to pick the files up the moment they exist. Re-run the generation
  when the service is back, then `python3 build.py`, commit, push.
- 2026-11-26: a typographic cover was built locally instead
  (`assets/cover.png`, 1600x2560, KDP-ideal) so the book has a real cover now
  and is ready for KDP. It is the cover in use on the site, the preview, and
  the EPUB. When the cartoonist cover is generated, drop it in as
  `assets/cover.png` and rebuild; nothing else changes.
- Chapters 3-10: write the prompt for each chapter the same way, one image
  per chapter, after the chapter itself is written and approved.
- 2026-11-26 10:23: second attempt, same result — the image service is
  still unavailable (upstream 503, three attempts each for cover, Ch1, Ch2).
  Do not keep retrying back-to-back; try again later (next session or
  tomorrow) and check the service is back first.
- 2026-11-26 10:38: third attempt (cover probe only), same 503. The service
  has now been down all morning. Do not retry again today unless the user
  asks; try once tomorrow, and if it is still down, leave it and check back
  the next day.
- 2026-11-26 11:34: service recovered. Cover and Chapter 1 and 2
  illustrations generated and checked visually; all three are good (title
  and author spelled correctly on the cover). The cartoonist cover replaced
  the typographic one as `assets/cover.jpg` (1600x2560, JPEG, padded from
  the generated 1280x1920 with the paper colour); the typographic cover is
  kept as `assets/cover-typographic.png`. Chapters 3-10 illustrations are
  being generated from the prompts above.
