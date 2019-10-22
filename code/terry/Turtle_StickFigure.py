from turtle import *

i = 0

while i < 100:
    forward(2)
    left(360 / 100)
    i = i + 1

right(90)
forward(90)
penup()
backward(60)
pendown()
startPosition = pos()
goto(startPosition[0]-25, startPosition[1]+4)
penup()
goto(startPosition[0], startPosition[1])
pendown()
goto(startPosition[0]+25, startPosition[1]+4)
penup()
goto(startPosition[0], startPosition[1])
forward(60)
startPosition = pos()
pendown()
goto(startPosition[0]-25, startPosition[1]-54)
penup()
goto(startPosition[0], startPosition[1])
pendown()
goto(startPosition[0]+25, startPosition[1]-54)

done()