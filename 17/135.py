min_number = None
max_number = None
for number in range(1812, 9286):
    if (number % 8 == 0 or number % 19 == 0) and (number % 4 != 0 and number % 9 != 0):
        first_digit = int(str(number)[0])
        if first_digit % 2 != 0:
            if min_number is None or number < min_number:
                min_number = number
            elif max_number is None or number > max_number:
                max_number = number
                
print(min_number, max_number)
