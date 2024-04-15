def f(n):
    n = list(map(int, n.split('.')))
    print('.'.join([f"{x:>08b}" for x in n]))

f('192.168.56.192')
f('255.255.255.192')
print()

f('192.168.56.208')
f('255.255.255.240')