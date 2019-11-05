'''
turtle lab continued
written by Rhornberger
last updated oct 22 2019
'''
from turtle import *
speed(100)
color('red', 'blue')
begin_fill()
bgcolor('black')
i = 0

while True:
    i += 1
    forward(200)
    left(170)
    if abs(pos()) < 1:
        print(i)
        break
end_fill()
penup()
left(30)
forward(200)
pendown()
#my_position = pos()
color('yellow', 'orange')
begin_fill()
i = 0
while True:
    i = i + 1
    forward(200)
    right(170)
    if i == 36:
        break
end_fill()
penup()
left(130)
forward(200)
pendown()
color('green', 'purple')
begin_fill()
i = 0
while True:
    i = i + 1
    forward(200)
    left(170)
    if i == 36:
        break
end_fill()
penup()
right(130)
forward(200)
pendown()
color('purple', 'green')
begin_fill()
i = 0
while True:
    i = i + 1
    forward(100)
    right(170)
    if i == 36:
        break
end_fill()
penup()
left(170)
forward(100)
pendown()
color('red', 'orange')
begin_fill()
edge_length = 0
i = 0
while i < 100:
    edge_length = edge_length + 1
    forward(edge_length)
    right(144)
    if edge_length == 100:
        break
end_fill()
#penup()
#left(190)
#forward(400)
#pencolor('green')
#pendown()

#end_fill()
done()