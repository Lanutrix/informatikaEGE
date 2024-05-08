a = 'йцукенгшщзхъфывапролджэячсмитьбюё'

count = set()
for i in a:
    for j in a:
        for k in a:
           for l in a:
               for m in a:
                   for n in a:
                       s = i+j+k+l+m+n
                       if s==s[::-1] and s.count('й')>=2 and 'йй' in s:
                            flag = 1
                            for x in range(6):
                               if s[x]=='й':
                                    if (x-1)>=0 and s[x-1]!='й':
                                       flag = 0
                                       break
                                    if (x+1)<6 and s[x+1]!='й':
                                       flag = 0
                                       break
                            if flag:
                               count.add(s)
print(len(count))