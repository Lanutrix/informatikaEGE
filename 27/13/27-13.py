Fin = open("27-13b.txt")

N = int( Fin.readline() )
L = 7
queue = []
for i in range(L):
  queue.append( int(Fin.readline()) )

count = 0
D = [[0, 0], [0, 0]]
for i in range(N-L):
  a = queue.pop(0)
  ind2 = 0 if a % 2 == 0 else 1
  ind7 = 0 if a % 7 == 0 else 1
  D[0][0] += 1
  D[0][1] += (1-ind7)
  D[1][0] += (1-ind2)
  D[1][1] += (1-ind2)*(1-ind7)
  x = int( Fin.readline() )
  queue.append( x )
  ind2 = 0 if x % 2 == 0 else 1
  ind7 = 0 if x % 7 == 0 else 1
  count += D[ind2][ind7]

print( count )

Fin.close()