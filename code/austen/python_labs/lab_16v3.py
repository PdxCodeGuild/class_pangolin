from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

draw.rectangle(((0, 0), (width, height)), fill="white")

# using the color pink
color = (139, 92, 74)  # brown
draw.line((250, 150, 250, 310), fill='black', width= 10) #body
draw.line((200, 230, 300, 230),fill='black', width= 5) #arms

draw.line((250, 310, 290, 400), fill='blue', width= 8)#legs
draw.line((250, 310, 210, 400), fill='blue', width= 8)#legs


circle_x = width/2
circle_y = height/3
circle_radius = 30
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill=color)

img.show()