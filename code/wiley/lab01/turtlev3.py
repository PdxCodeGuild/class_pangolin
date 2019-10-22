from turtle import *
i=0
while i < 100:
    if i%2 == 0:
        fillcolor('orange')
        begin_fill()
        pencolor('red')
    else:
        fillcolor('purple')
        begin_fill()
        pencolor('black')
    forward(120)
    right(177)
    forward (240)
    end_fill()
    i += 1
done()