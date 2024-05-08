def f(x,y):
    if x**2+y**2>=400:
        return 0
    n = [f(x+2,y), f(x, y+3)]
    t = [i for i in n if i<=0]
    if t:
        return -max(t)+1
    return -max(n)

for y in range(-1,20):
    p = f(5,y)
    if p==-2:
        print(y)