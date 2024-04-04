from collections import defaultdict

f = open('YandexVar2\\26.p.txt')
n,m = map(int, f.readline().split())

date = [[defaultdict(list) for i in range(24)]]*31
workers = [[0]]*n

for i in range(m):
    p = list(map(int,f.readline().split()))
    for j in range(p[2], p[2]+p[3]+1)