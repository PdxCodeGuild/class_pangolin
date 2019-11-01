'''
Image manipulation Lab 16
written by Rhornberger
last updated nov 01 2019
'''
from PIL import Image
img = Image.open('Lenna_(test_image).png')
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        
        #my code
        y = int(0.299*r + 0.587*g + 0.114*b)
        

        pixels[i, j] = (y,y,y)

img.show()