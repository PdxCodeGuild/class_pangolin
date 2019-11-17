from turtle import *

i = 0
# Draws a circle.
while i < 100:
    forward(2)
    left(360 / 100)
    i = i + 1

# Moves the turtle. And draws the body.
right(90)
forward(90)
penup()
backward(60)
pendown()
# Sets a variable to the turtle's current position.  This will be used as a reference.  All points will be in relation to this point.
startPosition = pos()
# Draws the arms.
goto(startPosition[0] - 25, startPosition[1] + 4)
penup()
goto(startPosition[0], startPosition[1])
pendown()
goto(startPosition[0] + 25, startPosition[1] + 4)
penup()
# Moves the turtle back to the center of the body
goto(startPosition[0], startPosition[1])
forward(60)
# Resets the turtles position variable, to the new, current position.
startPosition = pos()
pendown()
goto(startPosition[0] - 25, startPosition[1] - 54)
penup()
goto(startPosition[0], startPosition[1])
pendown()
goto(startPosition[0] + 25, startPosition[1] - 54)

done()
