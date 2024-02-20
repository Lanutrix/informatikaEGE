from string import ascii_lowercase
alf = 'yandex34'
alfavit = list(ascii_lowercase) + [str(i) for i in range(10)]
f = open('яндексВариант\\24.txt').read()
mx = 0
mask = [['y'],['a','4'],['n'],['e','3'],['x']]
for i in alfavit:
    if i not in alf:
        f = f.replace(i,' ')

for s in f.split():
    if s[0]=='y':
        n = 0
        ss = s.replace('yandex', '......').replace('y4ndex', '......').replace('yand3x', '......').replace('y4nd3x', '......')
        sss = ss.replace('.', ' ').split()
        if len(sss)==1:
            n = ss.count('.')
            for i in range(len(sss[0])):
                if sss[0][i] in mask[i]:
                    n+=1
                else:
                    break
        mx = max(mx, n)
print(mx)