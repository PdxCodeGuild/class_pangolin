#BieschkeLab16: Image Manipulator_v2.py 

import colorsys
from PIL import Image, ImageDraw

img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()
#manipulate hue, saturation, and and brightness
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        
        # colorsys uses colors in the range [0, 1]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        
        #there are no default values per se, so manipulate by just altering the var
        h = h*2
        s = s/2
        v = v/2
        # do some math on h, s, v
        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        # convert back to [0, 255]
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        pixels[i, j] = (r, g, b)

img.show()
