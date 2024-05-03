# На основе решения А. Кабанова

Fin = open("27-4b.txt")

N = int( Fin.readline() )

B = 5

sums = [0 for i in range(B)]
for i in range(N):
  ab = list(map( int, Fin.readline().split() ))
  sumsNext = [0]*B
  for s in sums:
    for x in ab:
      r = s + x
      if (i == 0 or s != 0) and  r > sumsNext[r%B]:
        sumsNext[r%B] = r
  sums = sumsNext[:]

Fin.close()

print( sums[0] )
