with open("27-186b.txt") as F:
  N, K = map( int, F.readline().split() )
  data = [int(x) for x in F]

sMax = float('-inf')
dataMax = float('-inf')
max2 = float('-inf')
for i in range(K, N):
  s = data[i] + max( dataMax + data[i-K], max2 )
  sMax = max( s, sMax )
  max2 = max( data[i]+data[i-K], max2 )
  dataMax = max( data[i-K], dataMax )

print( sMax )
