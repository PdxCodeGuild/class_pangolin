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

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="black")     # draw a black background

# some variables to help
body_width = 20
body_height = 170
leg_height = 100

# draw torso: a rectangle from x0, y0 to x1, y1
draw.rectangle(((240, 150), (240+body_width, 150+body_height)), fill="red")  # draw a blue shirt, 50 wide and 150 tall

# draw pants
draw.rectangle(((240, 320), (240+body_width, 320+leg_height)), fill="lightblue")
draw.rectangle(((240+(body_width//2),320+30), (242+(body_width//2),320+leg_height)), fill = 'black')

# draw arms
draw.rectangle(((160,200),(240,210)), fill="yellow")        # arms are 60 wide and 10 tall
draw.rectangle(((260,200),(340,210)), fill="yellow")


# # draw a line from x0, y0, x1, y1
# # using the color pink
# color = (256, 128, 128)  # pink
# draw.line((0, 0, width, height), fill=color)
# draw.line((0, height, width, 0), fill=color)


circle_x = width/2
circle_y = 120
circle_radius = 40
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

img.show()


# version 3: draw art
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