# AI Video Night

The AdaL AI Video Night deck (Tue 3 Nov 2026, 6 to 9 PM PT, AI Start Academy, San Francisco). Attendees build a launch video for their own SaaS product with AdaL.

Same design, flow and code as [jax-ship-it](https://github.com/jxspam/jax-ship-it) (launch-library theme, slide QR codes, agenda timer).

## Use it

- `site/index.html` is the finished deck: one self-contained file, open it in a browser.
- Keys: arrows or space to move, `f` fullscreen, `a` toggle the agenda panel.
- Agenda pill (top left) tracks the real PT clock and the time left in each section.
- Every slide shows a QR (top right) that opens that exact slide on the attendee's phone, plus a Discord QR.

## Make your own

- `base.css`, `extra.css`, `theme.css`: the design (theme.css carries the AdaL pink launch-library look).
- `deck.js`: navigation, agenda timer, per slide QR codes.
- `build.py`: assembles the slides into `site/index.html` (`python3 build.py`). The event kit (promo code, UTM links, Discord) and the agenda live at the top of the file.

## Submit your video

There is no submission form yet. Set `SUBMIT` near the top of `build.py` to the real link, then rerun `python3 build.py`. Until then the "Submit your video" slide shows a clearly marked placeholder.

## Deploy

```
cd site && vercel deploy --prod
```
