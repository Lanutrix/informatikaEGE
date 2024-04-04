print('x y w')
for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            if (x and (w<=y))==1:
                print(x,y,w)