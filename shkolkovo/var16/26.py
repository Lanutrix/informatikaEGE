f = open('shkolkovo\\var16\\26.txt')
n = int(f.readline())
f = sorted([list(map(int, i.split())) for i in f.readlines()])
print(f[:100])