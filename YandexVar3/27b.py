from functools import lru_cache
ra = ''.join(chr(1040+i) for i in range(32))
ra = ra[:6] + 'Ё' + ra[6:] + ' '

alf = {}
for i in range(1,35):
    alf[i]=ra[i-1]

f = open('YandexVar3\\27_B.txt').read().replace('10','И').replace('20','Т').replace('30','Ь')

@lru_cache
def fun(n, f):
    if len(n)==0:
        return 1
    if n[0].isdigit():
        if int(n[0])>3 or len(n)==1:
            return fun(n[1:], f+alf[int(n[0])])
        elif len(n)>=2 and n[:2].isdigit() and n[0].isdigit() and int(n[:2])<=34:
            return fun(n[1:], f+alf[int(n[0])]) + fun(n[2:], f+alf[int(n[0]+n[1])])
        elif n[:2].isdigit() and int(n[:2])>34 :
            return fun(n[1:], f+alf[int(n[0])])
        return fun(n[1:], f+n[0])
    else:
        return fun(n[1:], f+n[0])
print(fun(f,''))