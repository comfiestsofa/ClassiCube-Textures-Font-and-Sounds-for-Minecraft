#!/usr/bin/env python3
from PIL import Image
import os
import sys

def split_texture_atlas(image_path, tile_w, tile_h):
	# Load image
	img = Image.open(image_path)
	atlas_width, atlas_height = img.size

	# grid size
	cols = atlas_width // tile_w
	rows = atlas_height // tile_h

	print(f"Atlas size: {atlas_width}x{atlas_height}")
	print(f"Grid: {cols} cols x {rows} rows")

	base_name = os.path.splitext(os.path.basename(image_path))[0]
	output_dir = f"{base_name}-{tile_w}x{tile_h}"
	os.makedirs(output_dir, exist_ok=True)

	index = 0
	for row in range(rows):
		for col in range(cols):
			left = col * tile_w
			upper = row * tile_h
			right = left + tile_w
			lower = upper + tile_h

			tile = img.crop((left, upper, right, lower))
			output_path = os.path.join(output_dir, f"{index}-{col},{row}.png")
			tile.save(output_path)
			index += 1

	print(f"Saved {index} tiles to '{output_dir}'")

if __name__ == "__main__":
	if len(sys.argv) != 4:
		print("Usage: <image_path> <tile_width> <tile_height>")
		sys.exit(1)

	image_path = sys.argv[1]
	tile_width = int(sys.argv[2])
	tile_height = int(sys.argv[3])

	split_texture_atlas(image_path, tile_width, tile_height)
