from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")

circle_x = width / 2
circle_y = height / 2
circle_radius = 30
#draw.ellipse((circle_x - circle_radius, circle_y - circle_radius, circle_x + circle_radius, circle_y + circle_radius),fill=None, outline="black")
draw.ellipse((250 - circle_radius, 50 - circle_radius, 250 + circle_radius, 50 + circle_radius),fill=None, outline="black")

draw.line((250, 80, 250, 250), fill="black")
draw.line((170, 110, 330, 110), fill="black")
draw.line((250, 250, 280, 300), fill="black")
draw.line((250, 250, 220, 300), fill="black")

img.show()
