count = 0
min_num = None

for i in range(4413, 10154):
    if i % 5 == 0 and i % 23 == 0 and i % 7 != 0 and i % 10 != 0 and ((i // 10) % 10) in [1, 2, 3]:
        count += 1
        if min_num is None or i < min_num:
            min_num = i

print(count, min_num)
