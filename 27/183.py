f = open('27\\183\\27-183a.txt')
n,k = map(int, f.readline().split())
f = [int(i) for i in f.read().split()]

print(sorted(f[:k])[-4:])
print(sorted(f[k:])[-4:])
# m = 0
# for i in range(0,n-k):
#     m = max(m,sum(f[i:i+k]))

# print(m)