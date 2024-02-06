from itertools import *

def f(x,y,w,z):
    return (w and x and (not y)) == (x or y or (not z))

for a in product([0,1], repeat=7):
    table = [
    tuple([a[0], a[1], 0, 1, 1]),
    tuple([0, 1, a[2], 1, 1]),
    tuple([0, 1, a[3], a[4], 1]),
    tuple([0, a[5], 1, 1, a[6]])
]

    if len(table)==len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p,r))) for r in table] == [1,1,1,1]:
                print(p, table)