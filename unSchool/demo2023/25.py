g=0

for i in range(2023, 10**10, 2023):
    k = str(i)
    if k[0]=='1' and k[2:6] == '2139' and k[-1] == '4':
        print(k, i//2023)
