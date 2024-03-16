for n in range(5,1000):
    s = '1'+'2'*n
    while '1222' in s or '1212' in s or '132'in s:
        if '1222' in s:
            s = s.replace('1222','121',1)
        if '1212' in s:
            s = s.replace('1212','13',1)
        if '132' in s:
            s = s.replace('132','33',1)

    summ = sum(list(map(int, list(s))))
    if summ >1000:
        print(n, s)
        break