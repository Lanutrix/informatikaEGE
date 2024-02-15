print('y w x z')

for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                if not( (((not w) or y) == (x and (not z))) <= (y and x) ):
                    print(y, w, x, z)