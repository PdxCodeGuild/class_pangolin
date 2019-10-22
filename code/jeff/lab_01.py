# Lab_0.py
# Jeff Smith
# 10.21.19

from turtle import *

#form the head
i=0
while i < 100:
    forward(2)
    left(360/100)
    i = i + 1

right(90)
forward(50)
penup()
right(90)
forward(50)
left(180)
pendown()
forward(100)
penup()
left(180)
forward(50)
pendown()
left(90)
forward(100)
left(45)
forward(75)
penup()
left(180)
forward(75)
left(90)
pendown()
forward(75)

done()