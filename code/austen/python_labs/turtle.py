from turtle import *
#head circle

i = 0 
fillcolor('black')
begin_fill()

while i < 100:
    forward (2)
    left (360/100)
    i = i + 1

end_fill()

forward(0)#center
right(90) #rotate 90 degrees
forward(50) #body

#left arm
pensize(width= 10)
pencolor('red')
left(90)
forward(50)

#right arm
right(180)
forward(100)
right(180)
forward(50)

#lower body
right(90)
forward(50)

#left leg
pensize(width= 10)
pencolor('blue')
right(40)
forward(90)
left(180)
forward(90)

#right leg
right(100)
forward(90)

penup()
pensize(width=6)
pencolor('brown')
left(50)
forward(200)

pendown()
left(90)
forward(300)

pencolor('green')
c = 1
while c < 100:
    circle(50)
    right(20)
    c = c + 10
penup()

home()
right(220)
forward(250)

pendown()
pencolor('yellow')
edge_length = 50
s = 0
while s < 40:
    forward(100)
    right(100)
    edge_length+=20
    s = s+1
penup()
home()
done()


