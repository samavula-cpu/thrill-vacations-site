#!/usr/bin/env python3
"""
Regenerate the QR code embedded in book-direct-flyer.html.

The flyer's single QR code points guests to the "unlock direct offers" email
page on the live site, which then forwards them into the main site after
they submit their email:

    https://thrillvacations.com/#offer-all

Run this after changing the target URL, and it will:
  1. Generate a fresh QR code (high error correction, so it still scans
     if the printed flyer gets creased or smudged).
  2. Verify it decodes back to the expected URL (using OpenCV) before
     printing anything, so a broken code never ships.
  3. Print the base64 data-URI to paste into book-direct-flyer.html,
     replacing the existing `src="data:image/png;base64,...."` value on
     the <img class="qr-wrap"> tag.

Requirements:
    pip install qrcode[pil] opencv-python numpy
"""

import base64
import sys

import cv2
import numpy as np
import qrcode
from qrcode.constants import ERROR_CORRECT_H

TARGET_URL = "https://thrillvacations.com/#offer-all"
OUTPUT_PNG = "qr-combined.png"


def main():
    qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=10, border=2)
    qr.add_data(TARGET_URL)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#173B4C", back_color="white")
    img.save(OUTPUT_PNG)

    # Verify before handing back a data URI — never ship an unscannable code.
    with open(OUTPUT_PNG, "rb") as f:
        png_bytes = f.read()
    arr = np.frombuffer(png_bytes, dtype=np.uint8)
    cv_img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    decoded, _, _ = cv2.QRCodeDetector().detectAndDecode(cv_img)

    if decoded != TARGET_URL:
        print(f"QR verification FAILED. Decoded: {decoded!r}", file=sys.stderr)
        sys.exit(1)

    b64 = base64.b64encode(png_bytes).decode()
    print(f"Verified OK — QR decodes to {TARGET_URL}")
    print(f"Saved {OUTPUT_PNG}\n")
    print("Paste this as the src of the QR <img> in book-direct-flyer.html:\n")
    print(f"data:image/png;base64,{b64}")


if __name__ == "__main__":
    main()
