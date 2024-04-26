from fnmatch import fnmatch as mask

for i in range(0,10**9,2267):
    if mask(str(i), '7*15?3*7'):
        f = 1
        m = sum([int(j) for j in str(i)])
        for k in range(2,int(m**0.5)+1):
            if m%k==0:
                f = 0
                break
        if f:
            print(i, i//2267)
