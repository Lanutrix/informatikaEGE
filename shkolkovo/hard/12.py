for n in range(11,1050):
    s = '6'+'0'*n
    while '666' in s or '000' in s:
        if '666' in s:
            s = s.replace('666','00',1)
        else:
            s = s.replace('000','6',1)

    if s.count('0')==0 and len(s)>1:
        print(n)