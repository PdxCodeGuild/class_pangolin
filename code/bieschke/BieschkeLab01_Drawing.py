#1 Drawing with Turtle
import turtle
import math

t = turtle.Turtle()
t.color('brown')
s = turtle.Screen()
s.setup(1000, 1000)
s.bgpic('whale.gif')

def polygon(t, n, length):  #Calls turtle with n number of sides, each side being length number of pixels
    angle = 360 / n         #degrees in a circle divided by n number of sides
    
    t.fillcolor('red')
    t.begin_fill()

    i = 0
    for i in range(n):  
        t.fd(length) #forward 100 pixels
        t.lt(angle) #left turn at 90 degrees
        #t.bk(50) #back 50 pixels

    t.end_fill()

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

def spiral():
    #the power of speech
    n_sides = 8
    edge_length = 0

    z = 0
    while z < 50:
	    t.fd(edge_length)
	    t.rt(360/n_sides)
	    z = z + 1
	    edge_length = edge_length + 1

#head
t.penup()
t.setposition(0, 50)
t.pendown()
circle(t, 50)

#L arm
t.rt(90)
t.fd(50)
t.lt(120)
t.fd(70)

#R arm
t.penup()
t.home()
t.pendown()
t.seth(90)
t.lt(60)
t.fd(70)

#L leg
t.penup()
t.home()
t.pendown()
t.seth(270)
t.fd(75)
t.lt(45)
t.fd(75)

#R leg
t.penup()
t.home()
t.pendown()
t.seth(270)
t.fd(75)
t.rt(45)
t.fd(75)

#eyes
t.penup()
t.setposition(15, 115)
t.pendown()
circle(t, 5)
t.penup()
t.setposition(-15, 115)
t.pendown()
circle(t, 5)

#nose
t.penup()
t.setposition(0, 100)
t.seth(240)
t.pendown()
t.fd(10)
t.lt(90)
t.fd(10)

#R eyebrow
t.penup()
t.setposition(15, 125)
t.pendown()
t.seth(45)
t.fd(10)
t.rt(45)
t.fd(10)
t.lt(45)
t.fd(10)

#L eyebrow
t.penup()
t.setposition(-15, 125)
t.pendown()
t.seth(135)
t.fd(10)
t.lt(45)
t.fd(10)
t.rt(45)
t.fd(10)

#soap-polygon
t.penup()
t.setposition(-100, -125)
t.pensize(10)
t.pendown()
t.seth(270)
polygon(t, 4, 200)

#he has no mouth, yet he must scream
t.penup()
t.setposition(0, 75)
t.pendown()
t.pensize(1)
spiral()

x = input("What did you think of that?")
