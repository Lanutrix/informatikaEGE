from turtle import *

speed(0)
m = 70
left(90)

for i in range(4):
    forward(12*m)
    right(90)

for i in range(3):
    forward(12*m)
    right(120)

up()

for x in range(0, 13*m, m):
    for y in range(0, 13*m, m):
        goto(x,y)
        dot(3)
done()