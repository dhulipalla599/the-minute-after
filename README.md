# The Minute After

**Tagline:** One minute of thought, one small decent act, and the day gets better for everyone.

A book of life lessons in everyday situations: the moments when you know the
right thing and feel you can do nothing about it, and the one minute of
thought and one small decent move that would have made the day better for
everyone.

Each chapter is one situation, told as a short story: the moment, the
one-minute pause, the small better move, and why it worked.

## Voice

The book is written close to the heart, in the voice of a seasoned writer:
warm and plain, concrete in its detail, honest about what the narrator feels,
and restrained about telling the reader what to think. Show the moment, let
the feeling land, and let the lesson arrive on its own. Names are universal,
belonging to no one country: Mara, Daniel, Samuel. No name should anchor a
story to a single culture. Keep the chapter shape (the moment, the minute,
the better move, why it worked, one line to carry), but let each section
breathe as prose, not a list.

## Chapters

1. The Pressured Coworker (written)
2. The Helpless Person
3. The Meeting Where Nobody Speaks
4. The New Joiner Nobody Helps
5. The Angry Customer
6. The Blame That Lands on the Wrong Person
7. The Sharp Reply at Home
8. The Stranger in the Queue
9. The Burnt-Out Friend
10. The Day You Were the Difficult One

## One source, two outputs

The chapters live as Markdown in `chapters/`. That is the single source of
truth. From it, `build.py` produces both:

- **The website** in `docs/`: a plain static site, one page per chapter,
  with a contents page and previous/next navigation.
- **The Kindle book** as `book.epub`: built with pandoc from the same
  chapter files.

Build everything with:

```
python3 build.py
```

## Publish the website on GitHub Pages

1. Create a repository on GitHub (for example,
   `but-you-can-make-it-better`) and push this folder to it.
2. In the repository, go to Settings, Pages, and set the source to
   **Deploy from a branch**, branch `main`, folder **/docs**.
3. The book is live at
   `https://<your-github-username>.github.io/but-you-can-make-it-better/`.

Every new chapter is just a new Markdown file in `chapters/` followed by
`python3 build.py` and a push.

## Read it on a Kindle

1. Build the EPUB with `python3 build.py` (it writes `book.epub`).
2. Send it to your Kindle at
   [amazon.com/sendtokindle](https://www.amazon.com/sendtokindle), or email
   it to your Kindle address as an attachment. The EPUB appears in your
   Kindle library.
3. For a store-ready Kindle file, open `book.epub` in Amazon's free
   Kindle Previewer or Kindle Create, which converts it to KPF for
   Kindle Direct Publishing.
