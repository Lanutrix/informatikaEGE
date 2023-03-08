count = 0
min_number = None
for number in range(3712, 8433):
    binary = number%2
    quaternary = number%4
    if binary == quaternary and (number % 13 == 0 or number % 14 == 0 or number % 15 == 0):
        count += 1
        if min_number is None or number < min_number:
            min_number = number

print(count, min_number) 