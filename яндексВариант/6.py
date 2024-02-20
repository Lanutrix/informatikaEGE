from turtle import *

left(90)
speed(1)
delay(0)
m = 40

up()
right(30)
forward(4*m)
right(330)
down()

forward(4*m)
right(90)
forward(7*m)
right(45)
forward(4*m*(2**0.5))
right(135)
forward(11*m)
up()

for x in range(15):
    for y in range(15):
        goto(x*m,y*m)
        dot(4)

done()