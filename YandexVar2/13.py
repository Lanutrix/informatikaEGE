m = 0
for i in range(2**(5+8)):
    s = f'{i:>013b}'
    if s.count('1')==12:
        m+=1
print(m)