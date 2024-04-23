from fnmatch import fnmatch

c = 0

for i in range(1, 680_000):
    # print(fnmatch(str(i), '1*2*'))
    if fnmatch(str(i), '1*2*') and i%8==0:
        c+=1
print(c)