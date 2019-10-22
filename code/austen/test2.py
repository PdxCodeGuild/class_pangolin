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

home()#center
right(90) #rotate 90 degrees
forward(50) #body

#left arm
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
right(40)
forward(90)
left(180)
forward(90)

#right leg
right(100)
forward(90)

done()