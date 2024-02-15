for i in range(1,1000):
    for j in range(1,1000):
        s = '3' + '2'*i + '4'*j +'3'
        while '32' in s and '34' in s:
            s = s.replace('32', '44', 1)
            s = s.replace('34', '234', 1)
        if s.count('2')==36 and s.count('4')==47:
            print(i)