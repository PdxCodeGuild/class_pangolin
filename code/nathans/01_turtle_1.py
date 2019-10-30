# turtle_1.py


from turtle import *

speed(6)

fillcolor('purple')
begin_fill()

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

end_fill()

fillcolor('green')
begin_fill()
penup()
setposition(100,100)
pendown()
left(120)
forward(100)
left(120)
forward(100)
left(120)
forward(100)

end_fill()

penup()

setposition(50,0)
pendown()
fillcolor('blue')
begin_fill()

right(90)
forward(50)
left(90)
forward(75)
right(90)
forward(200)
right(90)
forward(150)
right(90)
forward(200)
right(90)
forward(75)

end_fill()

penup()

setposition(125,-100)

pendown()

pencolor('yellow')
forward(150)

penup()
setposition(-25,-100)
pendown()

left(180)
forward(150)
penup()

setposition(25,-250)
pendown()
left(90)
forward(200)
penup()
setposition(75,-250)
setheading(270)
pendown()

forward(200)


done()


