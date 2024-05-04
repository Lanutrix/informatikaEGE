from random import randint

N, K = 150_000, 97654
N, K = 200, 123

with open('27-184a.txt','w') as F:
   print( N, K, file=F )
   for i in range(N):
     print( randint(-randint(100, 10000), randint(100, 10000)), file=F )

