valid_numbers = []
for number in range(1221, 9764):
    if number % 7 == 0 and number % 2 != 0 and number % 5 != 0 and number % 11 != 0 and number % 49 != 0:
        valid_numbers.append(number)

count = len(valid_numbers)
max_number = max(valid_numbers)

print(count, max_number)
