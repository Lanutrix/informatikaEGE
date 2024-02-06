f = open('pro100ege3\\24_11892.txt').read()[:-1]
f = f.replace("Y", ' ').split()

cnt = set()
x = 0

for s in f:
    x = s.count('X')
    if x>=500:
        cnt.add(len(s))

print(cnt)
