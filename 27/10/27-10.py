Fin = open("27-10b.txt")

N = int( Fin.readline() )

mind, s = 20004, 0
for i in range(N):
  abc = [int(x) for x in Fin.readline().split()]
  m = max(abc)
  s += m
  for x in abc:
    if (m - x) % 4 != 0 and m-x < mind:
      mind = m - x
      # print( abc, m-x )

print(s, mind)

if s % 4 == 0:
  s -= mind

if s % 4 != 0:
  print( s )
else:
  print( 0 )

Fin.close()