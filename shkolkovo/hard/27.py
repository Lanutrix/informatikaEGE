f = open('shkolkovo\\hard\\27B.txt')

n = int(f.readline())

s1, s2, s3 = 0, 0, 0

for i in range(n):
    p = sorted(list(map(int, f.readline().split())))
    s1 += p[2]
    s2 += p[0]
    s3 += p[1]
print(s1, s2, s3)