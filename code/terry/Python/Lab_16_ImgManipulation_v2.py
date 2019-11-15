from PIL import Image
import colorsys

img = Image.open("lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        # y = 0.299 * r + 0.587 * g + 0.114 * b
        # enable these three variables to make it greyscale.
        # r = int(y)
        # g = int(y)
        # b = int(y)
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

        h = float(r/255)
        s = float(g/255)
        v = float(b/255)
        # print(h, s, v)
        #
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        print(h, s, v)
        #
        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)
        pixels[i, j] = (r, g, b)
img.show()
