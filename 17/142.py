divisible = []
for i in range(1412, 7866):
    if (i % 8 == 0 or i % 19 == 0) and i % 4 != 0 and i % 9 != 0 and sum(int(d) for d in str(i)) % 5 != 0:
        divisible.append(i)

min_divisible = min(divisible)
max_divisible = max(divisible)

print(min_divisible, max_divisible)
