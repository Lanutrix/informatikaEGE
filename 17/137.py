count = 0
min_num = None

for i in range(4565, 13347):
    if i % 7 == 0 and i % 6 != 0 and i % 3 != 0 and (i % 100) % 2 == 0:
        count += 1
        if min_num is None or i < min_num:
            min_num = i

print(count, min_num)
