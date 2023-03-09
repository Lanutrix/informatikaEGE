sum_num = 0
count = 0
max_num = None

for i in range(2381, 14656):
    if (i % 6 == 0 or i % 11 == 0) and i % 5 != 0 and i % 7 != 0 and (i // 100) % 10 != (i // 10) % 10:
        count += 1
        sum_num += i
        if max_num is None or i > max_num:
            max_num = i

average = sum_num / count

print(int(average), max_num)
