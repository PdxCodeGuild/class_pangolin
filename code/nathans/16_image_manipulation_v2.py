# 16_image_manipulation.py
###provided code
import colorsys
from PIL import Image
img = Image.open("lenna.png")
width, height = img.size
pixles = img.load()

for i in range(width):
        for j in range(height):
            r, g, b = pixles[i, j]
###my code goes here
### formula is   Y = 0.299*R + 0.587*G + 0.114*B
            # colorsys uses colors in the range [0, 1]
            
            # r = int(50)
            # g = int(501)
            # b = int(1)
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
#### values below are added to rotate hue, increase saturation, and decress brightness
            h -= .2
            s += .3
            v -= .4

           

            # do some math on h, s, v
            

            r, g, b = colorsys.hsv_to_rgb(h, s, v)

            # convert back to [0, 255]

            r = int(r*255)
            g = int(g*255)
            b = int(b*255)            
            
        #### my code below    
            # y = 0.299*r + 0.587*g + 0.114*b
            # r = int(y)
            # g = int(y)
            # b = int(y)

### code between this comment and the comment above is from v1
            pixles[i, j] = (r, g, b)
# img.save('greyscale.png')
img.show()




