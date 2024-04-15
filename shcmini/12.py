for n in range(11,1000):
    s = '3'+'7'*n
    while '37' in s or '577' in s or '7777' in s:
        if '37' in s:
            s = s.replace('37','7',1)
        if '577' in s:
            s = s.replace('577','73',1)
        if '7777' in s:
            s = s.replace('7777','5',1)
    sm = sum([int(i) for i in s])
    if sm==57 and s[-1]=='3':
        print(n)
        break