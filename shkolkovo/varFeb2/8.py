c1 = 0
for a1 in 'МОЩН':
    for a2 in 'МЩН':
        for a3 in 'МЩН':
            for a4 in 'МЩН':
                for a5 in 'МЩН':
                    for a6 in 'МОЩН':
                        if not( a1=='О' and a6=='О'):
                            c1+=1

c2 = 0
for b1 in 'ВЕБ':
    for b2 in 'ВЕБ':
        c2+=1
print(c1*c2)