for x in range(8):
    s = int(f'{x}1{x}',16)+int(f'{x}3{x}3',8)
    if s == 4096:
        print(x)