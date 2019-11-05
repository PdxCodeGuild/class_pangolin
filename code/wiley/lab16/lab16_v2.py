from PIL import Image
import os
import colorsys
img = Image.open(r"C:\Users\wiley\Documents\class_pangolin\code\wiley\lab16\lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()
#colorsys uses colors in the range [0,1]
#h, s, v = colorsys.rgb_to_hsv(r/225,g/255,b/255)

#do some math on h,s,v
#r, g, b = colorsys.hsv_to_rgb(h, s, v)

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        #Y = 0.299*R + 0.587*G + 0.114*B
        #y = round(r*.299) + round(g*.587)+ round(b*.114)

        h, s, v = colorsys.rgb_to_hsv(r/255,g/255,b/255)
        
        #print(h,s,v)
        h, s, v = (h+400),(s*1.93),(v-(v//2))


        r,g,b = colorsys.hsv_to_rgb(h,s,v)
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        pixels[i, j] = round(r),round(g),round(b)

img.show()

