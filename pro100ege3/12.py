for n in range(4,10_000):
    s = '5'+'2'*n

    while ('52' in s) or ('2222' in s) or ('1122' in s):
        if '52' in s:
            s = s.replace('52','11')
        elif '2222' in s:
            s = s.replace('2222','5')
        elif '1122' in s:
            s = s.replace('1122','25')
    
    r = sum(list(map(int, list(s))))
    if r == 64:
        print(n)