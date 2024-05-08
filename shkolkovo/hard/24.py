f = open('shkolkovo\\hard\\24.txt').read()
c = 1
# f = 'TooooooooooooUVVVWXYZUUoUTTTTTUUU'
# print(len('toooooooooooouv'))
# print('TTT'.count('TT'))
m = 0
for i in range(len(f)-2):
    p = f[i:i+2]
    if 'TT' not in p and 'VV' not in p:
        c+=1
    else:
        m = max(m,c)
        c = 1
print(m)