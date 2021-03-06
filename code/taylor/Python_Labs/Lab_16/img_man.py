# Taylor Rebbe 
# Lab_16
# 11/01/19

# v1
# from PIL import Image
# img = Image.open("lenna.png") # must be in same folder
# width, height = img.size
# pixels = img.load()

# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]
#         y = 0.299 * r + 0.587 * g + 0.114 * b
#         r,g,b = int(y),int(y),int(y)
#         pixels[i, j] = (r, g, b)

# img.show()
##################################################################################################################################
# v2

# from PIL import Image
# import colorsys

# img = Image.open("lenna.png") # must be in same folder
# width, height = img.size
# pixels = img.load()

# for i in range(width):
#     for j in range(height):
#         r, g, b = pixels[i, j]
#         # colorsys uses colors in the range [0, 1]
#         h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
#         h = h/6
#         # do some math on h, s, v
#         r, g, b = colorsys.hsv_to_rgb(h, s, v)
#         # convert back to [0, 255]
#         r = int(r*255)
#         g = int(g*255)
#         b = int(b*255)

#         pixels[i, j] = (r, g, b)

# img.show()

#################################################################################################################################
# v3
from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")

# draw a line from x0, y0, x1, y1
# using the color pink

draw.line((250,200, 250,400), fill=199)
draw.line((200,350, 300,350), fill=199)
draw.line((250,400, 200,475), fill=199)
draw.line((250,400, 300,475), fill=199)

circle_x = width/2
circle_y = height/2
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='red')

img.show()

##################################################################################################################################

# v3_+
# from PIL import Image, ImageDraw
# from random import randint

# width = 500
# height = 500

# img = Image.new('RGB', (width, height))
# draw = ImageDraw.Draw(img)

# for i in range(1000):
#     x0 = randint(0, width)
#     y0 = randint(0, height)
#     x1 = randint(0, width)
#     y1 = randint(0, height)
#     line_width = randint(1, 40)
#     red = randint(0, 255)
#     green = randint(0, 255)
#     blue = randint(0, 255)
#     draw.line((x0, y0, x1, y1), fill=(red, green, blue), width=line_width)

# img.show()