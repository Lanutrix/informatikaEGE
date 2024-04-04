a = int('3425604',22)
b = int('7284703',22)
c = a+b

p = 0
ans = 0

for x in range(22):
    for y in range(22):
        if (c+22*(x+y))%125==0 and (x+y)>p:
            p = x+y
            ans = (c+22*(x+y))//125
print(ans)