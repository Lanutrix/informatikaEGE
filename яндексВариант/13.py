k = 0
for a1 in ['0','1']:
    for a2 in ['0','1']:
        for a3 in ['0','1']:
            for a4 in ['0','1']:
                for a5 in ['0','1']:
                    s = '011'+a1+a2+a3+a4+a5
                    if ('111' not in s) and ('000' not in s):
                        k+=1
                        print(s)

print(k)