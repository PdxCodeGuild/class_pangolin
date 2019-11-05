import colorsys
from PIL import Image
img = Image.open("Lenna_(test_image).png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        # your code here
        h, s, v = h*20, s*10, v*40
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
    
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        pixels[i, j] = (r, g, b)
img.show()
