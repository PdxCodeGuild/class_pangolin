# Import the turtle library
from turtle import *

pensize(5)
# Create a circle / the stick-figure head
i = 0
while i < 100:
    forward(2)
    left(360/100)
    i = i + 1
# Turn the turtle right and begin drawing the body
right(90)
forward(50)
right(90)
forward(50)
# Creates the arms
right(180)
forward(100)
right(180)
forward(50)
# Creates the lower torso
left(90)
forward(50)
# Creates the legs
left(45)
forward(50)
right(180)
forward(50)
left(90)
forward(50)

done()
