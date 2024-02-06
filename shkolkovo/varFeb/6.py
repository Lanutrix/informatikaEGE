from turtle import *

left(90)
speed(100000)

# color('black', 'red')

m = 50

# begin_fill()
for i in range(5):
    forward(5*m)
    right(72)
# end_fill()
up()
for x in range(0, 10*m, m):
    for y in range(-5*m, 10*m, m):
        goto(x,y)
        dot(5)
done()
# canvas = getcanvas()
# cnt = 0
# for x in range(-200*m, 200*m, m):
#     for y in range(-200*m, 200*m, m):
#         item = canvas.find_overlapping(x,y,x,y)
#         if len(item)==1 and item[0]==5:
#             cnt+=1
# bye()
# print(cnt)