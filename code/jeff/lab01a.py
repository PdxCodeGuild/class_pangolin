# Lab_01a.py
# Jeff Smith
# 10.22.19
# attempted 'spirograph' using turtle star

from turtle import *

#change turtle color randomly
import random
Screen().bgcolor("black")
colors = ["blue","green","purple","red","yellow","orange"]
    #for count in range(10):
#    for i in range(2):
x = 200
y = 170
while True:
    forward(x)
    x = x+1
    left(y)
    y = y+1
    color(random.choice(colors))


#    if abs(pos()) < 1:
#        break

done()