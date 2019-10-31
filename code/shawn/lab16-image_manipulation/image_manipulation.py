# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 16 - Image Manipulation
# Date: 10/31/2019



from PIL import Image


img = Image.open("Lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        # your code here    
        y = int(0.299*r) + int(0.587*g) + int(0.114*b)
        r = g = b = y

        pixels[i, j] = (r, g, b)

img.show()
