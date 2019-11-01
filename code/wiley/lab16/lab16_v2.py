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
        r, g, b = pixels[(i*2345)%512, j]
        #Y = 0.299*R + 0.587*G + 0.114*B
        #y = round(r*.299) + round(g*.587)+ round(b*.114)
        h, s, v = colorsys.rgb_to_hsv(r,g,b)
        #print(h,s,v)
        h, s, v = (h),(s),(v)

        r,g,b = colorsys.hsv_to_rgb(h,s,v)

        pixels[i, j] = round(r),round(g),round(b)

img.show()

