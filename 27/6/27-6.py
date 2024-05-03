Fin = open("27-6b.txt")

N = int( Fin.readline() )

max6 = 0
maxX = 0
max2 = 0
max3 = 0
for i in range(N):
  x = int( Fin.readline() )
  if x % 6 == 0 and x > max6:
    if max6 > maxX: maxX = max6
    max6 = x
  else:
    if x > maxX: maxX = x
    if x % 2 == 0 and x > max2: max2 = x
    elif x % 3 == 0 and x > max3: max3 = x

R = max( max6*maxX, max2*max3 )

print( max6, maxX, max6*maxX )
print( max2, max3, max2*max3 )
print( R )

Fin.close()