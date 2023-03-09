divisible_numbers = []
for number in range(4855, 7857):
    if number % 6 == 0 and number % 15 == 0 and number % 7 != 0 and number % 16 != 0:
        hundreds, tens = number//100%10, number//10%10
        if (hundreds + tens) % 2 == 0:
            divisible_numbers.append(number)

average = int(sum(divisible_numbers)) // len(divisible_numbers)
max_number = max(divisible_numbers)
min_number = min(divisible_numbers)
print(average+min_number+max_number)
