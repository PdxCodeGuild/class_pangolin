#filename stick_man.py
from turtle import *
pencolor("purple")
fillcolor("purple")
speed(7)
pensize(3)

left(90)
forward(30)
right(90)
begin_fill()
i = 0
while i < 100:
    forward(2)
    left(360/100)
    i = i + 1
end_fill()
right(90)
forward(30)
right(45)
forward(50)
right(180)
forward(50)
right(90)
forward(50)
right(180)
forward(50)
left(135)
forward(60)
right(30)
forward(70)
left(180)
forward(70)
right(120)
forward(70)
done()