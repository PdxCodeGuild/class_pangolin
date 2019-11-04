# lab_16.py
# Image manipulation
# Jeff Smith
'''
Use the formula for converting to greyscale and the code below. Remember that Pillow uses ints for RGB values, in the range of 0-255, whereas your math will often use floats. 'Y' is used to represent the brightness. The following formula get the brightness of an RGB triplet. To convert to greyscale, set R, G, and B to Y.

Y = 0.299*R + 0.587*G + 0.114*B
'''

from PIL import Image
img = Image.open("lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        y = int(0.299*r + 0.587*g + 0.114*b)

        pixels[i, j] = (y, y, y)
img.show()
