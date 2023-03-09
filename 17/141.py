sum_num = 0
count = 0
min_num = None

for i in range(4391, 9876):
    if (i % 11 == 0 or i % 17 == 0) and i % 2 != 0 and i % 13 != 0 and (i // 100) % 2 == 0 and (i // 10) % 2 != 0:
        sum_num += i
        count += 1
        if min_num is None or i < min_num:
            min_num = i

avg_num = int(sum_num / count)

print(avg_num, min_num)
