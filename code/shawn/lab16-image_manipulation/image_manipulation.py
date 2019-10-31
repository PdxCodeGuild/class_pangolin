# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 16 - Image Manipulation
# Date: 10/31/2019


import colorsys
import random 
from PIL import Image, ImageDraw

# Version 1 (greyscale)
img = Image.open("Lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        # your code here    
        y = int(0.299*r) + int(0.587*g) + int(0.114*b)
        r = g = b = y

        pixels[i, j] = (r, g, b)

img.show()

# Version 2 (HSV....rotate hue, increase saturation, lower brightness)
img = Image.open("Lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        # colorsys uses colors in the range [0, 1]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        # do some math on h, s, v
        h += 0.3
        s += 0.3
        v -= 0.3

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        # convert back to [0, 255]

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        pixels[i, j] = (r, g, b)

img.show()

# Version 3: Draw Stick Figure and 1000 random lines/rectangles

# 1000 random lines: 
width = 500
height = 500

img = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(img)

for i in range(1000):
    x0 = random.randint(0, width)
    y0 = random.randint(0, height)
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    line_width = random.randint(1, 40)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    draw.line((x0, y0, x1, y1), fill=(red, green, blue), width=line_width)

img.show()