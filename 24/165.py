ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open("24-164.txt") as F:
  data = F.readlines()
  maxK = 0
  for s in data:
    k, currK = 1, 1
    for i in range(1,len(s)):
      if s[i] == s[i-1]:
        currK += 1
        k = max(k, currK)
      else:
        currK = 1
    if k > maxK:
      maxK = k
      ma, letterMax = 0, ''
      for letter in ABC:
        cnt = s.count(letter)
        if cnt > ma:
          ma, letterMax = cnt, letter

print( letterMax,
       sum(s.count(letterMax) for s in data) )