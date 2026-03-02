#!/usr/bin/env python3
from PIL import Image
import os
import re

# (classicube folder, filename, tile size, vanilla folder)
folders = [
	("classicube/accented-9x12", 
	 "accented.png", 
	 (9, 12),
	 "minecraft/accented-9x12"),
	
	("classicube/nonlatin_european-8x8", 
	 "nonlatin_european.png", 
	 (8, 8),
	 "minecraft/nonlatin_european-8x8")
]

tile_pattern = re.compile(r"(\d+)-(\d+),(\d+)\.png") # index-x,y.png

for classicube_folder, output_name, tile_size, vanilla_folder in folders:
	width_tile, height_tile = tile_size

	tiles = {}
	max_x = max_y = 0

	# get tiles from classicube folder
	for file in os.listdir(classicube_folder):
		match = tile_pattern.match(file)
		if match:
			index, x, y = match.groups()
			x, y = int(x), int(y)
			img = Image.open(os.path.join(classicube_folder, file))
			tiles[(x, y)] = img
			max_x = max(max_x, x)
			max_y = max(max_y, y)

	# supplement any missing tiles from vanilla folder
	for file in os.listdir(vanilla_folder):
		match = tile_pattern.match(file)
		if match:
			_, x, y = match.groups()
			x, y = int(x), int(y)
			if (x, y) not in tiles:
				ref_img = Image.open(os.path.join(vanilla_folder, file))
				tiles[(x, y)] = ref_img
			# update max number of tiles based on vanilla, not on classicube
			max_x = max(max_x, x)
			max_y = max(max_y, y)

	# make empty texture atlas
	final_width = (max_x + 1) * width_tile
	final_height = (max_y + 1) * height_tile
	final_img = Image.new("RGBA", (final_width, final_height), (0, 0, 0, 0))

	# paste in tiles
	for (x, y), tile_img in tiles.items():
		final_img.paste(tile_img, (x * width_tile, y * height_tile))

	final_img.save(output_name)
	print(f"generated {output_name} ({final_width}x{final_height})")
