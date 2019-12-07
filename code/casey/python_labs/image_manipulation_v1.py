'''
Lab 16: Image Manipulation - Version 1

Purpose/goal: Convert an image into greyscale using the Pillow library, which is a fork of PIL 'python image library'.

    - Use the formula for converting to greyscale and the code below. - D

    - Remember that Pillow uses ints for RGB values, in the range of 0-255, whereas your math   will often use floats. - D

    - 'Y' is used to represent the brightness. The following formula get the brightness of an   RGB triplet. To convert to greyscale, set R, G, and B to Y. - D

'''

# import image from PIL
from PIL import Image

# define / open lenna.png
img = Image.open("lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        y = 0.299*r + 0.587*g + 0.114*b

        pixels[i, j] = (round(y), round(y), round(y))

img.show()