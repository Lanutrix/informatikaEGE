from fnmatch import fnmatch

for x in range(17_253, 10 ** 9 + 1, 17_253):
    s = str(x)
    if fnmatch(s, '8?4*2?9*8'):
        print(x, x // 17_253)