from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGBA', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill=("grey"))

# draw a rectangle from x0, y0 to x1, y1
#draw.rectangle(((250, 250), (600, 600)), fill="lightblue")

# draw a line from x0, y0, x1, y1
# using the color pink
color = (256, 128, 128)  # pink

#line starts at x250,y150 and ends at x250 y400
#this is the "body"
draw.line((250,150, 250, 400 ), fill=color, width = 10)

#line starts at x150, y250 and ends at x350, y250
#these are "arms"
draw.line((150, 250, 350, 250), fill='red', width = 10) 

#this is the head.  The start of the ellipse is at x220,y90 and the end is at x280,y150.  
#These coordinates correspond to a rectangle that the ellipse is built within. 
draw.ellipse((220, 90, 280, 150), fill='yellow', width = 10)

#this is the left leg.  It starts at x , y  and ends at x, y 
draw.line((250,400,150,500), fill='blue', width = 10)

#this is the right leg.  It starts at x, y  and ends at x , y . 
draw.line((250,400,330,500), fill = 'purple', width = 10)
#draw.line(())
img.show()