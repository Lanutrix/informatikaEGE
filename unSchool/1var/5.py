for i in range(10_000, 100_000):
    n = str(i)
    s1 = int(n[0])+int(n[2])+int(n[4])
    s2 = int(n[1])+int(n[3])
    r = str(min(s1, s2)) + str(max(s1, s2))
    if r == '723':
        print(i)
        break