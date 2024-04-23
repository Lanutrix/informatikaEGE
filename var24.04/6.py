from turtle import *
left(90)
speed(0)
m = 50

for i in range(2):
    forward(10*m)
    right(90)
    forward(18*m)
    right(90)
up()
forward(5*m)
right(90)
forward(14*m)
left(90)
down()
for i in range(2):
    forward(17*m)
    right(90)
    forward(7*m)
    right(90)
up()

for x in range(14*m, 19*m, m):
    for y in range(5*m, 11*m, m):
        goto(x,y)
        dot(6)

done()