# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 1 - Turtle (stickman)
# Date: 10/22/2019

from turtle import *
import time

# print paramater to console for testing
print(color())

# set higher speed
speed(10)

# set background pic
bgpic('background.gif')

# # startup pause to allow to move draw window to second monitor
#  time.sleep(5)

# function for drawing circle, given (x,y) starting point and a radius
def drawCircle(x,y,radius,color):

    fillcolor(color)
    begin_fill()
    goto(x,y)
    pendown()
 
    i = 0
    while i < 100:
        forward(radius)
        left(360/100)
        i = i + 1

    penup()
    end_fill()

# draw head
drawCircle(0,0,2,'yellow')

# upper body
pendown()
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
drawCircle(-20,30,.3,'blue')

# draw right eye
drawCircle(15,30,.3,'blue')

# draw mouth
goto(-20,15)
setheading(0)
pendown()
forward(40)
penup()

# use cursor as nose
goto(0,30)
fillcolor('red')
setheading(90)


# finish drawing
done()

