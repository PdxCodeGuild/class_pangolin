'''
image manipulation lab version 3
written by Rhornberger
last updated nov 1 2019
'''
from PIL import Image, ImageDraw
width = 500
height = 500
img = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(img)

# stolen from class notes
'''
# draw.rectangle(((0,0), (width, height)), fill = "white")
# draw.rectangle(((100,100),(300,300)), fill = "lightblue")
# color = (256, 128, 128)
# draw.line((0,0, width, height), fill = color)
# draw.line((0, height, width, 0), fill = color)

# circle_x = width / 2
# circle_y = height / 2
# circle_radius = 100
# draw.ellipse((circle_x - circle_radius, circle_y - circle_radius, circle_x + circle_radius, circle_y + circle_radius), fill = "lightgreen")
# img.show()
'''
# stick figure
'''
circle_x = width / 2
circle_y = height / 3
circle_radius = 50
draw.ellipse((circle_x - circle_radius, circle_y - circle_radius, circle_x + circle_radius, circle_y + circle_radius), fill = "lightgreen")
#(x, y) (x, y)
draw.line(((250,125), (250, 320)), fill = 'lightgreen')
draw.line(((200, 250), (300, 250)), fill = 'lightgreen')
draw.line(((250,320),(180, 420)), fill = 'lightgreen')
draw.line(((320, 420),(250, 320)), fill = 'lightgreen')
img.show()
'''
from random import randint
#1000 lines of random 
for i in range(1000):
    x0 = randint(0, width)
    y0 = randint(0, height)
    x1 = randint(0, width)
    y1 = randint(0, height)
    line_width = randint(1,40)
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    draw.line((x0, y0, x1, y1), fill =(red, blue, green), width = line_width)
    img.show()
