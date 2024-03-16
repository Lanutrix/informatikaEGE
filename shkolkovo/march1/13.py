def f(n:str):
    print('.'.join([f'{x:>08b}' for x in list(map(int, n.split('.')))]))

f('35.92.220.29')
f('35.92.128.0')
print(int('10000000',2))