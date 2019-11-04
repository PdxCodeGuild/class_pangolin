####16_image_manipulation_v3.py

from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")

### body rectangle
draw.rectangle(((200, 150), (300, 350)), fill="teal", outline="pink")
### left leg
draw.rectangle(((225, 350), (230, 450)), fill="magenta")
### right leg, outline used 
draw.rectangle(((270, 350), (275, 450)), fill="orange", outline="purple")
### testing "width" argument in draw.line
draw.line(((0, 0), (0, 500)), fill="orange", width=10)
# draw a line from x0, y0, x1, y1
# using the color pink
### kept to have a nice way to track the center of drawn image
### comment out 3 lines below to remove the X
color = (256, 128, 128)  # pink rgb values
draw.line((0, 0, width, height), fill=color)
draw.line((0, height, width, 0), fill=color)

### center the circle
circle_x = width/2
### adjust height of circle
circle_y = 100
# size of circle
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')
### added to show coding difference from circle above
draw.ellipse((0, 0, 100, 100), fill="brown")
img.show()