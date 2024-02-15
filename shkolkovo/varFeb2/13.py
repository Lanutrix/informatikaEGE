def ips(s:str):
    ss = list(map(int, s.split('.')))
    return '.'.join([f'{x:>08b}' for x in ss])

print(ips("20.105.130.175"))
print(ips("20.105.128.0"))