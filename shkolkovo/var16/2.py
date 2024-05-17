print('x y w z')

for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                if not ( ((not z) == x) <= (y==(x or w)) ):
                    print(x,y,w,z)