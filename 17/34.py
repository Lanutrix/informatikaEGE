min_num = None
max_num = None

for i in range(1000, 10000):
    if i % 3 != 0 and i % 17 != 0 and i % 19 != 0 and  4**5 <= i < 4**6:
        if max_num is None or i > max_num:
            max_num = i
        if min_num is None or i < min_num:
                min_num = i

print(min_num, max_num)
