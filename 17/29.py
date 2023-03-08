max_number = 0
total_sum = 0
for number in range(2807, 8559):
    if number%2 == 1 and (number//2)%2 == 1 and number % 9 == 5:
        total_sum += number
        if number > max_number:
            max_number = number

print(max_number, total_sum)
