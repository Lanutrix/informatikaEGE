valid_numbers = []
for number in range(1012, 9639):
    if number % 3 == 0 and number % 11 != 0 and number % 13 != 0 and number % 17 != 0 and number % 19 != 0:
        valid_numbers.append(number)

count = len(valid_numbers)
max_number = max(valid_numbers)

print(count, max_number)
