count = 0
min_number = None
for number in range(2477, 7850):
    if number % 2 == 0 and number % 5 != 0 and number % 8 != 0 and number % 9 != 0 and number % 13 != 0:
        count += 1
        if min_number is None or number < min_number:
            min_number = number

print(count, min_number)
