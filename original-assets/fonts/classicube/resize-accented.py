#!/usr/bin/env python3
from PIL import Image
import os

accented_font_dir = "accented-9x12"

# top padding of 3, bottom padding of 1 is how we get matching rendering with ClassiCube
top_pad = 3
bottom_pad = 1
left_pad = 0
right_pad = 1

for filename in os.listdir(accented_font_dir):
	if filename.endswith(".png"):
		img_path = os.path.join(accented_font_dir, filename)
		img = Image.open(img_path)

		new_width = img.width + left_pad + right_pad
		new_height = img.height + top_pad + bottom_pad

		new_img = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))
		new_img.paste(img, (left_pad, top_pad))

		new_img.save(img_path)
