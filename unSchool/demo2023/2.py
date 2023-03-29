print('w x y z f')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not(not(y <= x) or (z <= w) or not(z)):
                    print(w, x, y, z, 0)