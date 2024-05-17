s = 'ВОЗДУХ'
llm = [sorted(['В','У']),sorted(['Х','У']),sorted(['В','О']),sorted(['Х','О'])]
cnt = 0
for i in s:
    for j in s:
        for k in s:
            for l in s:
                for m in s:
                    n = i+j+k+l+m
                    if n.count('О')==1 and n.count('У')==0 or n.count('О')==0 and n.count('У')==1:
                        f = 1
                        for g in range(4):
                            ss = sorted(n[g:g+2])
                            if ss==llm[0] or ss==llm[1] or ss==llm[2] or ss==llm[3]:
                                f = 0
                                break
                        if f:
                            cnt+=1
print(cnt)