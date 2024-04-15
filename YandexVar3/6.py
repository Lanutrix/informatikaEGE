from turtle import *

left(90)
speed(0)
m = 100

for i in range(12):
    forward(1*m)
    right(36)
up()
# forward(4*m)
# right(90)
# down()
# for i in range(8):
#     forward(6*m)
#     right(90)

# up()

for x in range(0*m, 4*m, m):
    for y in range(-1*m, 3*m, m):
        goto(x,y)
        dot(3)
done()