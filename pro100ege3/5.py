for i in range(100,1000):

    s = str(i)
    f = [int(s[0])*int(s[1]), int(s[2])*int(s[1])]
    f = sorted(f)
    f = int(''.join(list(map(str,f))))

    if f==621:
        print(i)