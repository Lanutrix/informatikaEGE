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
      mi, letterMin = 10**10, ''
      for letter in ABC:
        cnt = s.count(letter)
        if cnt > 0 and cnt <= mi:
          mi, letterMin = cnt, letter

print( letterMin,
       sum(s.count(letterMin) for s in data) )