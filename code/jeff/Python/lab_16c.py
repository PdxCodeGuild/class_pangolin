from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(img)

# # draw a line from x0, y0, x1, y1                     
# # using the color pink
# color = (256, 128, 128)  # pink
# draw.line((0, 0, width, height), fill=color)
# draw.line((0, height, width, 0), fill=color)


circle_x = width/2
circle_y = height/2
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

color = (256, 128, 128)  # pink
draw.line(((250, 300), (250, 420)), fill=color)
draw.line(((200, 320), (300, 320)), fill=color)
draw.line(((250, 420), (300, 480)), fill=color)
draw.line(((250, 420), (200, 480)), fill=color)


img.show()