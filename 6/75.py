from turtle import *
speed(1000)
m = 33

left(90)

for i in range(10):
    for h in range(4):
        forward(4*m)
        right(90)
    back(6*m)
    right(90)


up()
for x in range(-10*m, 10*m, m):
    for y in range(-10*m, 7*m, m):
        goto(x,y)
        dot(2)

done()