alf = 'ОБРУЧ'

c = 0

for a1 in alf:
    for a2 in alf:
        for a3 in alf:
            for a4 in alf:
                for a5 in alf:
                    s = a1+a2+a3+a4+a5

                    if s.count("Р")>=2 and s.count("РР")==0:
                        c+=1

print(c)