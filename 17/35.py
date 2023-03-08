count = 0
sum_numbers = 0
min_number = None
max_number = None

for number in range(1476, 7040):
    if number % 2 == 0 and number % 16 != 0 and (number // 10) % 10 >= 4:
        count += 1
        sum_numbers += number
        if min_number is None or number < min_number:
            min_number = number
        if max_number is None or number > max_number:
            max_number = number

    average = (min_number + max_number) / 2

print(count, int(average))