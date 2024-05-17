s = '0'*40 + '7'*40 + '0'*43

while '07' in s or '700' in s:
    if '07' in s:
        s = s.replace('07', '7', 1)
    else:
        s = s.replace('700', '0', 1)
print(s)