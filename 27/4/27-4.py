Fin = open("27-4b.txt")

D = 5

N = int( Fin.readline() )

s, dMin  = 0, [10001]*D
for i in range(N):
  a, b = map( int, Fin.readline().split() )
  s += max( a, b )
  d = abs( a-b )
  r = d % D
  if r > 0:
    dMinNew = dMin[:]
    for k in range(1, D):
      r0 = (r + k) % D
      dMinNew[r0] = min( d+dMin[k], dMinNew[r0] )
    dMinNew[r] = min( d, dMinNew[r] )
    dMin = dMinNew[:]

if s % D == 0:
  print( s )
else:
  print( s, s%D )
  print( dMin )
  print( s - dMin[s % D] )

Fin.close()