# Draw stick figure

from turtle import *

i = 0
while i < 100:
    forward(2)
    left(360/100)
    i = i + 1

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

done()