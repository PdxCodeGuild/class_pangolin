# Lab_01a.py
# Jeff Smith
# 10.22.19
# attempted 'spirograph' using turtle star

from turtle import *
color('purple', 'green')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
setheading(90)
forward(10)
setheading(0)

color('green', 'purple')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()