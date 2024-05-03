import time

Fin = open("27-6b.txt")

N = int( Fin.readline() )

start = time.perf_counter()

data = []
for i in range(N):
  data.append( int( Fin.readline() ) )
Fin.close()

R = 0
for i in range(N):
  for j in range(i):
    p = data[i]*data[j]
    if p % 6 == 0 and p > R:
      R = p

print( R )

end = time.perf_counter()
print(end - start)