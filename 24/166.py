with open("24-164.txt") as F:
  A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  ss = F.readlines()
  maxSpan = 0
  for s in ss:
    if s.count('G') < 15:
      for c in A:
        i = 0
        while i < len(s) and s[i] != c:
           i += 1
        j = len(s)-1
        while j > 0 and s[j] != c:
           j -= 1
        maxSpan = max(maxSpan, j -i)

print( maxSpan )