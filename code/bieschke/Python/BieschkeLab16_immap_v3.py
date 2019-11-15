#BieschkeLab16: Image Manipulator_v3.py 

import colorsys
from PIL import Image, ImageDraw
'''
img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        #r = round(0.299*r)
        #g = round(0.587*g)
        #b = round(0.114*b)
        
        # colorsys uses colors in the range [0, 1]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        
        #there are no default values per se, so manipulate by just altering the var
        h = h*2
        s = s*2
        v = v*2
        # do some math on h, s, v
        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        # convert back to [0, 255]
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)


        pixels[i, j] = (r, g, b)

draw = ImageDraw.Draw(img)
draw.text([0, 0], text="All Your Base", fill=512)
draw.text([0, 0], text="All Your Base", fill=512)
del draw

img.show()
'''

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

# the origin (0, 0) is at the top-left corner
#this rectangle is the background picture
draw.rectangle(((0, 0), (width, height)), fill="white")

# draw a rectangle from x0, y0 to x1, y1
#draw.rectangle(((100, 100), (300, 300)), fill="lightblue")

# draw a line from x0, y0, x1, y1
# using the color pink
#color = (256, 128, 128)  # pink
color = "red"
draw.line([(.5, 1), (1,1)], fill=color)
#draw.line((0, height, width, 0), fill=color)

circle_x = width/2
circle_y = height/2
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

img.show()
