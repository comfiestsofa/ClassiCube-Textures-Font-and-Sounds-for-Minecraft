#!/usr/bin/env python3
from PIL import Image

base = Image.open("../../original-assets/bedrock-samples/resource_pack/textures/gui/icons.png").convert("RGBA")
overlay = Image.open("textures/ui/sprites/hud/crosshair.png").convert("RGBA")
position = (0, 0)
base.paste(overlay, position)
base.save("textures/gui/icons.png")
