with open("27-184b.txt") as F:
  N, K = map( int, F.readline().split() )
  data = [int(x) for x in F]

sMax = float('-inf')
maxK = float('-inf')
max1 = max2 = max3 = float('-inf')
for i in range(N):
  if i >= K:
    maxK = max( data[i-K], maxK )
    s = maxK + data[i]
    s += max1+max2 if maxK != max1 else max2+max3
    sMax = max( s, sMax )
  if data[i] > max1:
    max1, max2, max3 = data[i], max1, max3
  elif data[i] > max2:
    max2, max3 = data[i], max2
  elif data[i] > max3:
    max3 = data[i]

print( sMax )
