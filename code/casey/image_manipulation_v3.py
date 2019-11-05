'''
Lab 16: Image Manipulation - Version 3

Pillow can also be used to draw, the code below demonstrates some functions that Pillow provides. Use these functions to draw a stick figure. You can find more documentation here.

'''

from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="coral")

# draw a rectangle from x0, y0 to x1, y1
draw.rectangle(((280, 203), (220, 340)), fill="lightblue")

# draw a line from x0, y0, x1, y1
# using the color lightblue
color = (173, 216, 230)  # lightblue
draw.line((220, 207, 150, 300), fill=color, width=8)
draw.line((280, 207, 350, 300), fill=color, width=8)
draw.line((222, 340, 220, 450), fill=color, width=8)
draw.line((278, 340, 281, 450), fill=color, width=8)

circle_x = width/2
circle_y = height/3
circle_radius = 35
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightblue')

img.show()