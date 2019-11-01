from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGBA', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill=("white"))

# draw a rectangle from x0, y0 to x1, y1
#draw.rectangle(((250, 250), (600, 600)), fill="lightblue")

# draw a line from x0, y0, x1, y1
# using the color pink
color = (256, 128, 128)  # pink
draw.line((height//2,width//2, 0,40000 ), fill="black")
#draw.line((0, height, width, 0), fill="black")


circle_x = 100
circle_y = 100
circle_radius = 50
#draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, 250), fill='lightgreen')

img.show()