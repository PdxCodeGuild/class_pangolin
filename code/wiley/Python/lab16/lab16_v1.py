from PIL import Image
import os
img = Image.open(r"C:\Users\wiley\Documents\class_pangolin\code\wiley\lab16\lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        #Y = 0.299*R + 0.587*G + 0.114*B
        #r = round(r*.299)
        #g = round(g*.587)
        #b = round(b*.114)
        y = round(r*.299) + round(g*.587)+ round(b*.114)




        pixels[i, j] = (y,y,y)

img.show()

