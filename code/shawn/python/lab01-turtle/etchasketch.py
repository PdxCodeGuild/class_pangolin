# Shawn Stolsig
# PDX Code Guild 
# Assignment: Lab 1 - Turtle (extra shapes)
# Date: 10/22/2019

from turtle import *

# # size of increment
moveDistance = 25


##################
## Ability to change increment distance not seeming to work properly 
## due to global variable.  Address later!
##################
# # increase moveDistance
# def moveMore():
#     global moveDistance

#     if moveDistance == 0:
#         moveDistance = 10
#     if moveDistance == 10:
#         moveDistance = 25
#     if moveDistance == 25:
#         moveDistance = 50
#     if moveDistance == 50:
#         moveDistance = 100
#     print("your move distance is now " + str(moveDistance))

# # decrease moveDistance
# def moveLess():
#     global moveDistance

#     if moveDistance == 100:
#         moveDistance = 50
#     if moveDistance == 50:
#         moveDistance = 25
#     if moveDistance == 25:
#         moveDistance = 10
#     if moveDistance == 10:
#         moveDistance = 0
#     print("your move distance is now " + str(moveDistance))

# define direction functions
def moveUp():
    setheading(90)
    forward(moveDistance)

def moveDown():
    setheading(270)
    forward(moveDistance)

def moveWest():
    setheading(180)
    forward(moveDistance)

def moveEast():
    setheading(0)
    forward(moveDistance)


# declare function for changing pen state
def changePen():
    if isdown():
        penup()
        print("your pen is now up!")
    else:
        pendown()
        print("your pen is now down!")

# declare function for clearing board
def clearWindow():
    clear()

# init the pen
pendown()

# event listeners
onkey(moveUp, 'Up')
onkey(moveDown, 'Down')
onkey(moveEast, 'Right')
onkey(moveWest, 'Left')
onkey(changePen, 'd')
onkey(clearWindow, 'c')
# to use when changing increment distance
# onkey(moveMore, 'q')
# onkey(moveLess, 'a')
listen()

# print instructions to alert window
print("\n***************************************\n** Welcome to a basic etch-a-sketch! **\n***************************************")
print("Controls: \n Arrow keys for direction \n c to clear board \n d to raise/lower pen")
done()