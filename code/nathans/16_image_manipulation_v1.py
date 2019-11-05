# 16_image_manipulation.py
###provided code
from PIL import Image
img = Image.open("lenna.png")
width, height = img.size
pixles = img.load()

for i in range(width):
        for j in range(height):
            r, g, b = pixles[i, j]
###my code goes here
### formula is   Y = 0.299*R + 0.587*G + 0.114*B
            

            
            y = 0.299*r + 0.587*g + 0.114*b
            r = int(y)
            g = int(y)
            b = int(y)

### code between this comment and the comment above is only additional code entered
            pixles[i, j] = (r, g, b)
# img.save('greyscale.png')
img.show()




