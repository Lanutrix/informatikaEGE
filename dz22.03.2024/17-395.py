dt = [int(x) for x in open('17-390.txt')]

lst = [x for x in dt if abs(x) % 1000 == 615]
sred = sum(lst) / len(lst)

results = []
for i in range(len(dt)-2):
  t = dt[i:i+3]
  num4 = len([x for x in t if 1000 <= abs(x) <= 9999])
  div5 = len([x for x in t if abs(x) % 5 == 0])
  div7 = len([x for x in t if abs(x) % 7 == 0])
  okEnd = len([x for x in t if x > sred])
  if (1 <= num4 <= 2 and div5 > div7 and okEnd == 3):
    results.append(sum(t))

print(len(results), min(results))
