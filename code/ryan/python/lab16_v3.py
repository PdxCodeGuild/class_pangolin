from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

circle_x = width/2
circle_y = height/2
circle_radius = 50

draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')
draw.rectangle(((240, 300), (260, 400)), fill="lightblue")

img.show()