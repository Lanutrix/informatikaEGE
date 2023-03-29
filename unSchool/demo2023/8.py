from itertools import product

nums = product('01234567', repeat=5)
k = 0
for i in nums:
    num = ''.join(i)
    if num.count('6') == 1 and num[0]!='0':
        if '16' not in num and '36' not in num and '56' not in num and '76' not in num and \
            '61' not in num and '63' not in num and '65' not in num and '67' not in num:
            k += 1

print(k)