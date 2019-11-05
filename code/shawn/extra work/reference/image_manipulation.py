# https://github.com/PdxCodeGuild/class_pangolin/blob/master/1%20Python/labs/lab16-image_manipulation.md

# good website for colors: colorizer.org

# good library to use for image manipulation is Pillow, then importanting Image from it
from PIL import Image

# To calculate brightness of a pixel, where r/g/b are ints (and y is an int representing brightness)
r = g = b = 120
y = int(0.299*r) + int(0.587*g) + int(0.114*b)

# HSV is very useful for actually doing things with colors, since you can keep the same color 
# while adjusting saturation and brightness with seperate numbers
# use colorsys for HSV 
import colorsys

# to open an image
img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()


for i in range(width):
    for j in range(height):
        # unpacks r,g,b values from current pixel
        r, g, b = pixels[i, j]

        # colorsys uses colors in the range [0, 1]
        # convert rbg values to hsv
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        # do some math on h, s, v
        h += 0.3            # this "rotates" hue 
        s += 0.3            # this increases saturation
        v -= 0.3            # this lowers brightness

        # hsv back to rgb in range [0,255]
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        # loads rbg values back into current pixel
        pixels[i, j] = (r, g, b)

# display image
img.show()