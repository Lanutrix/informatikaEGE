from turtle import *

left(90)
speed(100)
m = 30

for i in range(2):
    forward(8*m)
    right(90)
    forward(18*m)
    right(90)
up()

forward(4*m)
right(90)
forward(10*m)
left(90)
down()

for i in range(2):
    forward(17*m)
    right(90)
    forward(7*m)
    right(90)
up()

for x in range(10*m, 20*m, m):
    for y in range(3*m, 10*m, m):
        goto(x,y)
        dot(9)

done()