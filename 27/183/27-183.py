with open("27-183a.txt") as F:
  N, K = map( int, F.readline().split() )
  data = [int(x) for x in F]

sMax = float('-inf')
maxK = float('-inf')
max1 = max2 = float('-inf')
for i in range(N):
  if i >= K:
    maxK = max( data[i-K], maxK )
    s = maxK + data[i]
    s += max1 if maxK != max1 else max2
    sMax = max( s, sMax )
  if data[i] > max1:
    max1, max2 = data[i], max1
  elif data[i] > max2:
    max2 = data[i]

print( sMax )
