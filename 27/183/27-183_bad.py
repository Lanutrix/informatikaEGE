with open("27-183a.txt") as F:
  N, K = map( int, F.readline().split() )
  data = [int(x) for x in F]

sMax = float('-inf')
for i in range(N):
  for j in range(i+1,N):
    for m in range(max(j+1,i+K),N):
      s = data[i] + data[j] + data[m]
      if s > sMax:  sMax = s

print( sMax )
