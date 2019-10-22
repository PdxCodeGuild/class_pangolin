from turtle import *
fillcolor('yellow')
begin_fill()
i = 0
#build the head
while i < 100:
    forward(2)
    left(360/100)
    i = i + 1
end_fill() # end face color
right(90) #turn 'down'
forward(100)# body
right(45)# right leg
forward(80)#right leg
backward(80)#back up the right leg
left(90)#left leg
forward(80) #left leg  
backward(80)#back up left leg
left(135)#back to body
forward(50)
left(90)#left arm
forward(50)
backward(100)#reverse for right arm
done()
