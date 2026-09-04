# Thrill Vacations

Source code for the Thrill Vacations direct-booking website (thrillvacations.com)
and its printable "Book Direct" flyer, for two vacation rentals:

- **White Sands** — Panama City Beach, FL
- **Blue Sands** — Murrells Inlet, SC

## Structure

```
index.html                          The entire live site — single self-contained
                                     HTML file (hash-routed: #home, #white-sands,
                                     #blue-sands, #offer-all, etc.)
flyer/
  book-direct-flyer.html            Printable 8.5x11in "Book Direct" flyer with
                                     a QR code, ready to open in a browser and
                                     print/export to PDF.
  generate_qr.py                    Regenerates the flyer's QR code if the
                                     target URL ever changes.
source-photos/
  blue-sands-elevator.jpg           Original photos used on the Blue Sands page
  blue-sands-exterior-3floor.jpg    (already embedded as base64 in index.html —
                                     kept here for reference/reuse).
```

## The site (`index.html`)

A single HTML file with client-side hash routing that simulates a
multi-page site — no build step, no framework, no server required.

Key features:

- Home page, and full listing pages for each property
- Live booking via the [Hospitable](https://hospitable.com) Direct booking
  widget (currently connected for White Sands; Blue Sands still needs to be
  connected in Hospitable)
- QR-code landing pages (`#offer-white`, `#offer-blue`, `#offer-all`) that
  capture a guest's email via a [Netlify Forms](https://docs.netlify.com/manage/forms/)
  submission before forwarding them into the site — used for the printed
  flyer's QR code

### Deploying

The site is currently hosted on [Netlify](https://netlify.com) at
thrillvacations.com.

**Manual deploys** (current process): drag-and-drop `index.html` onto the
Netlify dashboard, or into the site's Deploys tab.

**Recommended: connect this repo to Netlify instead.** Netlify can deploy
automatically on every push to this repo, which removes the "forgot to
redeploy" step that's caused a few mix-ups (QR codes / forms appearing not
to work simply because the latest `index.html` hadn't been uploaded yet).
To switch: in the Netlify dashboard, go to **Site configuration → Build &
deploy → Link repository**, connect this GitHub repo, and leave the build
command empty with `index.html` as the publish directory (root).

**Important — Netlify Forms after connecting a repo:** Netlify's automatic
form detection scans the HTML at deploy time. After connecting the repo,
double-check under **Forms → Usage and configuration** that "Form
detection" is still enabled, then trigger one deploy — this is the same
setting that had to be turned on manually before.

## The flyer (`flyer/book-direct-flyer.html`)

Self-contained 8.5x11in printable flyer. Open it in a browser and print (or
"Save as PDF") — the page is sized with `@page` so it prints as a single
clean page with no browser margins needed.

It has one QR code that takes guests to `#offer-all` on the live site (the
"unlock direct offers" email-capture page for both properties). If that
target URL ever needs to change, run:

```bash
pip install qrcode[pil] opencv-python numpy
python3 flyer/generate_qr.py
```

It regenerates the code, verifies it decodes correctly, and prints a
base64 data-URI to paste into the flyer's QR `<img>` tag.

## Contact

sam.avula@thrillvacations.com · (650) 605-5899
# thrill-vacations-site
# thrill-vacations-site
# thrill-vacations-site
