with open('D:\\informatikaEGE\\unSchool\\24.txt') as fl:
    dt = fl.readline()
    dt = dt.replace("O", "A").replace("D", "C").replace("F", "C")
    dt = dt.replace("CA","P")
    val = 0
    vals = []
    for i in dt:
        if i=="P":
            val+=1
        else:
            vals.append(val)
            val = 0
print(max(vals))