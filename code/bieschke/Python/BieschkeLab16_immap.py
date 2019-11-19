#BieschkeLab16: Image Manipulator.py 
#Greyscale an imported image
from PIL import Image

img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        r = round(0.299*r)
        g = round(0.587*g)
        b = round(0.114*b)
        
        #print("what\'s happening here?")
        pixels[i, j] = (r, g, b)

img.show()