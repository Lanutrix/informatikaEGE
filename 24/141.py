with open("24-s1.txt") as file:

  k = 0
  while True:
    s = file.readline()
    if not s: break
    s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in s1:
      stroka = "F"+x+"O"
      if s.count(stroka)>0:
        k +=1
        break
  print(k)
