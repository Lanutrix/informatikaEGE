f = open('shkolkovo\\varFeb2\\24-1__1voqb.txt').readlines()
c = 1
cnt = 0
for i in f:
    if c%2==1:
        if len(i)%2==1:
            if i.count('A')%3==0 and i[len(i)//2:].count('M') <= i[len(i)//2:].count('O'):
                if i[:len(i)//2].count('AR') >= i[len(i)//2:].count('PARK'):
                    cnt += 1
    c+=1

print(cnt)
