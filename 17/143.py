numbers = []

for num in range(4735, 8757):
    if num % 5 == 0 and num % 17 == 0 and num % 7 != 0 and num % 14 != 0 and (num // 10) % 10 >= (num // 100) % 10:
        numbers.append(num)

avg = sum(numbers) // len(numbers)
max_num = max(numbers)
min_num = min(numbers)

result = avg + max_num + min_num
print(result)
