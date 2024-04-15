P = {1, 3, 9, 13, 17, 29, 35, 51, 42}
Q = {2, 3, 13, 35, 36, 39, 42, 51, 67}
A = []
for i in range(1,70):
    if (i not in P) and i in Q:
        A.append(i)
print(len(A))