dt = [int(x) for x in open('17-390.txt')]

ls = [ x for x in dt if abs(x) % 100 == 28 ]
sr = sum(ls) / len(ls)

results = []
for i in range(len(dt)-2):
  t = dt[i:i+3]
  num4 = len( [x for x in t if 1000 <= abs(x) <= 9999] )
  lt = len( [x for x in t if abs(x) % 100 == 11] )
  ok = len( [x for x in t if x > sr] )
  if (num4 >= 1 and lt == 2 and ok == 3 ):
    results.append( sum(t) )

print( len(results), min(results) )
