# Turtle lab - Free draw
# This would be good to convert to functions. For example, draw circle and draw line.
from turtle import *

color("blue")

i = 0
j = 0
k = 0
m = 0
n = 0
p = 0
q = 0

# Circle 1
while i < 100:
    forward(2)
    left(360 / 100)
    i = i + 1

# Line
right(90)
forward(100)
right(90)

# Circle 2
while j < 100:
    forward(2)
    left(360 / 100)
    j = j + 1

# Move turtle 90 degrees down the arch
while k < 25:
    forward(2)
    left(360 / 100)
    k = k + 1

# Line
right(90)
forward(100)
right(90)

# Circle 3
while m < 100:
    forward(2)
    left(360 / 100)
    m = m + 1

# Move turtle 90 degrees down the arch
while n < 25:
    forward(2)
    left(360 / 100)
    n = n + 1

# Line
right(90)
forward(100)
right(90)

# Circle 4
while p < 100:
    forward(2)
    left(360 / 100)
    p = p + 1

# Move turtle 90 degrees down the arch
while q < 25:
    forward(2)
    left(360 / 100)
    q = q + 1

# Line
right(90)
forward(100)
right(90)

done()
