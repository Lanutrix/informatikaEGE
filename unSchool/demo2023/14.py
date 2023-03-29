alph = '0123456789abcde'

for x in alph:
    f = int(f'123{x}5', 15) + int(f'1{x}233', 15)
    if f % 14 == 0:
        print(f//14)
        break