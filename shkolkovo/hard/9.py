f = open('shkolkovo\\hard\\9.txt')
n = 24263
cnt = 0

for i in range(n):
    s = f.readline()
    p = list(map(int, s.split()))
    if '0' in s:
        s1 = sum([i for i in p if p.count(i)>1])
        s2 = sum([i for i in p if p.count(i)==1])
        if abs(s1-s2)<20:
            print(p)
            cnt+=1

print(cnt)