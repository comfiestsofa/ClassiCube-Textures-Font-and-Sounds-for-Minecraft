#!/usr/bin/env python3
from PIL import Image

def remove_matching_pixels(image1_path, image2_path, output_path, tolerance=0):
	img1 = Image.open(image1_path).convert("RGBA")
	img2 = Image.open(image2_path).convert("RGBA")

	if img1.size != img2.size:
		raise ValueError("Images must be the same size")

	pixels1 = img1.load()
	pixels2 = img2.load()

	width, height = img1.size

	for y in range(height):
		for x in range(width):
			r1, g1, b1, a1 = pixels1[x, y]
			r2, g2, b2, a2 = pixels2[x, y]

			if (
				abs(r1 - r2) <= tolerance and
				abs(g1 - g2) <= tolerance and
				abs(b1 - b2) <= tolerance
			):
				# Make transparent
				pixels1[x, y] = (r1, g1, b1, 0)

	img1.save(output_path, "PNG")
	print(f"Saved result to {output_path}")

remove_matching_pixels("ore-overlays/original/coal_ore.png", "ore-overlays/original/stone.png", "ore-overlays/coal_ore.png", tolerance=24)
remove_matching_pixels("ore-overlays/original/copper_ore.png", "ore-overlays/original/stone.png", "ore-overlays/copper_ore.png", tolerance=24)
remove_matching_pixels("ore-overlays/original/copper_ore.png", "ore-overlays/original/stone.png", "ore-overlays/copper_ore.png", tolerance=24)
remove_matching_pixels("ore-overlays/original/diamond_ore.png", "ore-overlays/original/stone.png", "ore-overlays/diamond_ore.png", tolerance=24)
remove_matching_pixels("ore-overlays/original/emerald_ore.png", "ore-overlays/original/stone.png", "ore-overlays/emerald_ore.png", tolerance=24)
remove_matching_pixels("ore-overlays/original/gold_ore.png", "ore-overlays/original/stone.png", "ore-overlays/gold_ore.png", tolerance=24)
remove_matching_pixels("ore-overlays/original/iron_ore.png", "ore-overlays/original/stone.png", "ore-overlays/iron_ore.png", tolerance=24)
remove_matching_pixels("ore-overlays/original/lapis_ore.png", "ore-overlays/original/stone.png", "ore-overlays/lapis_ore.png", tolerance=24)
remove_matching_pixels("ore-overlays/original/redstone_ore.png", "ore-overlays/original/stone.png", "ore-overlays/redstone_ore.png", tolerance=24)

remove_matching_pixels("dirt-overlays/original/podzol_side.png", "dirt-overlays/original/dirt.png", "dirt-overlays/podzol_side_overlay.png", tolerance=0)
remove_matching_pixels("dirt-overlays/original/dirt_path_side.png", "dirt-overlays/original/dirt.png", "dirt-overlays/dirt_path_side_overlay.png", tolerance=0)
remove_matching_pixels("dirt-overlays/original/coarse_dirt.png", "dirt-overlays/original/dirt.png", "dirt-overlays/coarse_dirt_overlay.png", tolerance=0)
remove_matching_pixels("dirt-overlays/original/mycelium_side.png", "dirt-overlays/original/dirt.png", "dirt-overlays/mycelium_side_overlay.png", tolerance=0)
remove_matching_pixels("dirt-overlays/original/rooted_dirt.png", "dirt-overlays/original/dirt.png", "dirt-overlays/rooted_dirt_overlay.png", tolerance=0)
