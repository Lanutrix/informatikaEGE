min_num = None
max_num = None

for i in range(2121, 13470):
    if i % 3 == 0 and i % 15 == 0 and i % 6 != 0 and i % 12 != 0 and (i // 100) % 10 % 3 == 0:
        if min_num is None or i < min_num:
            min_num = i
        if max_num is None or i > max_num:
            max_num = i

print(min_num + max_num)
