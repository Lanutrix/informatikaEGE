from turtle import *

m = 60
speed(0)

for i in range(9):
    forward(2*m)
    right(45)
    forward(2*m)
    left(90)

up()

for x in range(-1*m,10*m,m):
    for y in range(-4*m,10*m,m):
        goto(x,y)
        dot(3)
done()