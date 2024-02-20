for n in range(4,10000):
    s = '1'+n*'6'
    while '111' in s or '66' in s:
        if '6666' in s:
            s = s.replace('6666', '1', 1)
        else:
            s = s.replace('111','3', 1)
        if '66' in s:
            s = s.replace('66', '6', 1)
    if s.count('3')>=5:
        print(n)
        break
