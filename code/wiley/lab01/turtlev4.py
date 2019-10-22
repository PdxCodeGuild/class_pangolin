from turtle import *
bgpic('pangolin.gif')#set background 
pencolor('white')
pensize(20)
#creating 'H' text
def h():
    penup(),goto(100,200),pendown(),right(90),forward(100),backward(50),left(90),forward(50),left(90),forward(50),backward(100)
h()
#creating 'i' text
def i():
    penup(),goto(180,100),pendown(),forward(70),penup(),forward(25),pendown(),circle(4)
i()
done()