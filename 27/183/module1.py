from random import randint

N, K = 150_000, 97654
N, K = 500, 123

with open('27-182a.txt','w') as F:
   print( N, K, file=F )
   for i in range(N):
     print( randint(-randint(100, 10000), randint(100, 10000)), file=F )

