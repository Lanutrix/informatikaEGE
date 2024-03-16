alf = 'ЕВКЛИД.'
c = 0
from itertools import product

for i in product(alf, repeat=7):
    w = ''.join(i)

    p = w.split('.')
    # print(p)
    if len(p)==2 and len(p[0])!=0 and len(p[1])!=0:
        right = 1 if ( (p[1].count('ИЕ') == 0) and 'В' not in p[1] and 'К' not in p[1] and 'Л' not in p[1] and 'Д' not in p[1]) else 0
        left  = (p[0].count('Е')+p[0].count('И'))==(p[0].count('В')+p[0].count('К')+p[0].count('Л')+p[0].count('Д'))
        if right and left:
            c+=1
print(c)
