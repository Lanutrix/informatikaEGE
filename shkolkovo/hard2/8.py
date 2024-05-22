s = sorted('БАКР')
c = 0
f = 0
for i in s:
    for j in s:
        for k in s:
            for l in s:
                w = i+j+k+l
                if f:
                    c+=1
                if w=='КРАБ':
                    f = 1
                if w=='БРАК':
                    f = 0

print(c)