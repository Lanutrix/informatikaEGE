P = {2, 7, 14, 28, 34, 102}
Q = {7, 12, 24, 28, 56, 94}

a = set()

for i in Q:
    if i not in P:
        a.add(i)

print(sum(a))