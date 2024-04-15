ra = ''.join(chr(1040+i) for i in range(32))
ra = ra[:6] + 'Ё' + ra[6:] + ' '

alf = {}
for i in range(1,35):
    alf[i]=ra[i-1]

f = open('YandexVar3\\27_A.txt').read()

def fun(n, f):
    if len(n)==0:
        return 1
    if int(n[0])>3 or len(n)==1 and n[:2] not in ['10','20','30']:
        return fun(n[1:], f+alf[int(n[0])])
    elif len(n)>=2 and n[:2] not in ['10','20','30']:
        return fun(n[1:], f+alf[int(n[0])]) + fun(n[2:], f+alf[int(n[0]+n[1])])
    elif n[:2] in ['10','20','30']:
        return fun(n[2:], f+alf[int(n[0]+n[1])])
print(fun(f,''))