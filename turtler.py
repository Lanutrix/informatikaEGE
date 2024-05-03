g = set()

def f(n,s):
    if s==10:
        global g
        g.add(n)
        return
    if abs(n)!=n:
        f(abs(n),s+1)
    if n>0 and (n-10)<0 or n<0 and (n-10)>0:
        f(n-10,s+1)
    f(n*(-2),s+1)

f(1,0)
print(len(g))