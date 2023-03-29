import sys

sys.setrecursionlimit(100000)

def f(x, y):
    if x<y and x==33:
        return 0
    elif x == y:
        return 1
    return f(x+1, y) + f(x*2, y) + f(x*3, y)

print(f(3,15) * f(15, 50))