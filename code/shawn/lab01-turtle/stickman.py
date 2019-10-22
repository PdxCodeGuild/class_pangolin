# Draw stick figure

from turtle import *

# function for drawing circle, given (x,y) starting point and a radius
def drawCircle(x,y,radius):
    goto(x,y)
    pendown()
    i = 0
    while i < 100:
        forward(radius)
        left(360/100)
        i = i + 1
    penup()

# i = 0
# while i < 100:
#     forward(2)
#     left(360/100)
#     i = i + 1
drawCircle(0,0,2)

pendown()
# upper body
right(90)
forward(50)

# right arm
right(90)
forward(50)

# left arm 
left(180)
forward(100)

# back to body
right(180)
forward(50)

# down to start of legs
left(90)
forward(50)

# left leg
right(45)
forward(50)

# back to body
left(180)
forward(50)

#lef right leg
right(90)
forward(50)

penup()

# draw left eye
drawCircle(-20,30,.3)

# draw right eye
drawCircle(15,30,.3)

# draw mouth
goto(-20,15)
setheading(0)
pendown()
forward(40)
penup()

# use cursor as nose
goto(0,30)
setheading(90)


done()

