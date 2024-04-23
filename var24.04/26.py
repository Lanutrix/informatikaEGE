f = open('var24.04\\26.txt')
b, z = map(int, f.readline().split())

f1 = [list(map(int, f.readline().split())) for i in range(z)]
f1 = sorted(f1)
f2 = [[i[0],i[1]+i[0]] for i in f1]
f2 = f2.sort(lambda x: x[1], x[0])


print(f1[:100], f2[:100])