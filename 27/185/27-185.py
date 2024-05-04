with open("27-185b.txt") as F:
  N, K = map( int, F.readline().split() )
  data = [int(x) for x in F]

sMax = float('-inf')
data_i = [ (x,i) for i, x in enumerate(data) ]
indMax3 = [ i for x, i in sorted(data_i, reverse=True) ][:3]

for i in range(K, N):
  ind3 = [ m for m in indMax3
             if m not in [i, i-K] ][0]
  s = data[i] + data[i-K] + data[ind3]
  sMax = max( s, sMax )

print( sMax )
