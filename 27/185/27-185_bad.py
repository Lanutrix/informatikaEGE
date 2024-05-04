with open("27-185a.txt") as F:
  N, K = map( int, F.readline().split() )
  data = [int(x) for x in F]

sMax = float('-inf')
for i in range(N-K):
  for j in range(i+1,N):
    for m in range(j+1,N):
      if j == i+K or m == j+K or m == i+K:
        s = data[i] + data[j] + data[m]
        if s > sMax:
          sMax = s
          print( s, data[i], data[j], data[m] )

print( sMax )
