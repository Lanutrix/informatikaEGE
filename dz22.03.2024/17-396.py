dt = [int(x) for x in open('17-390.txt')]

lst = [x for x in dt if abs(x) % 1000 == 641]
sd = sum(lst) / len(lst)

results = []
for i in range(len(dt)-2):
  t = dt[i:i+3]
  num = len([x for x in t if 10000 <= abs(x) <= 99999])
  d5 = len([x for x in t if abs(x) % 5 == 0])
  d11 = len([x for x in t if abs(x) % 11 == 0])
  ok = len([x for x in t if x > sd])
  if (1 <= num <= 2 and d5 > d11 and ok == 3):
    results.append(sum(t))

print(len(results), min(results))
