min_num = float('inf')
max_num = float('-inf')

for num in range(1000, 10000):
    if num % 5 != 0 and num % 7 != 0 and num % 11 != 0:
        if 3**7 <= num < 3**8:
            if num < min_num:
                min_num = num
            if num > max_num:
                max_num = num

print(min_num, max_num)
