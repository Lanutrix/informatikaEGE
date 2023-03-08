valid_numbers = []
for number in range(1200, 11201):
    if number % 5 == 0 and number % 7 != 0 and number % 13 != 0 and number % 17 != 0 and number % 19 != 0:
        valid_numbers.append(number)

count = len(valid_numbers)
min_number = min(valid_numbers)

print(count, min_number)
