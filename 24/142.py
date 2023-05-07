with open("24-s1.txt") as file:
  k = 0
  while True:
    f = file.readline()
    if not f: break
    s1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in s1:
      stroka = "A"+x+"R"
      if f.count(stroka)>0:
        k +=1
        break
  print(k)