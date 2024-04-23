f = open('var24.04\\24.txt').read()
f = f.replace('NPO', '+').replace('PNO', '+').replace('O', ' ').replace('P', ' ').replace('N', ' ')
f = f.split()
print(max([len(i) for i in f]))