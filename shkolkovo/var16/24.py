f = open('shkolkovo\\var16\\24.txt').read()
# f = 'AANEFEHHHHEFLL'
# print(len('FEHHHHE'))
c = 1
mx = 0
for i in range(len(f)-1):
    p = f[i:i+2]
    if p!='EF':
        c+=1
    else:
        mx = max(mx, c)
        c = 1
print(mx)