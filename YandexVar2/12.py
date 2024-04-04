m = 0

for n in range(4,10000):
    s = '9'+'6'*n
    while '666' in s or '9909' in s or '66' in s:
        s = s.replace('666','999',1)
        s = s.replace('9909','6',1)
        s = s.replace('66','0',1)
    if len(s)==10:
        m = n
print(m)