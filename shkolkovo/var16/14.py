for x in range(17):
    s = int(f'3700102',17)+int(f'802719',17)+x*17**3+x*17**4
    if s%11==0:
        print(x)