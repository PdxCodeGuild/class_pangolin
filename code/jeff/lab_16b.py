#lab_16b.py
#Photo manipulation Version 2
#Jeff Smith

# Use the colorsys library to increase the saturation, decrease the brightness, and rotate the hue. Colorsys represents colors as floats in the range 0.0 - 1.0, whereas pillow uses ints in the range 0 - 255. You'll have to convert between these two representations.

import colorsys
from PIL import Image
img = Image.open("lenna.png")
width, height = img.size
pixels = img.load()

# r = .2
# g = .2
# b = .1
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
       
        h = .4 * h
        s = .3 * s
        v = .8 * v

        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)
        pixels[i, j] = (r, g, b)

img.show()