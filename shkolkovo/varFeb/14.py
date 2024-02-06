f = 6**180 + 6**60 - 356 + 6**15

fs = ''

while f>0:
    fs += str(f%6)
    f //= 6

d = []

for i in range(1,6):
    d.append(fs.count(str(i)))

print(d)