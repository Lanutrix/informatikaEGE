print('a b c d')

for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                if not(((a and b)<=c) and ((b and c)<=d)):
                    print(a,b,c,d)