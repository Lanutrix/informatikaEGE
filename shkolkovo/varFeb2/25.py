# Заметим, что 7 нечетных делителей имеют числа вида (p**6) * (2**x), где p - простое число,  
# а x - любое целое неотрицаельное  
left = 1000  # Задаю границы цикла  
right = 123456789  
ans = 0  # Будущий ответ  
simple = [True] * (int(right ** (1 / 6)) + 1)  
numbers = []  
# Найдем все простые числа, которые меньше корня 6 степени от правой границы  
for i in range(2, len(simple)):  
    if simple[i]:  
        numbers.append(i)  
        for j in range(i + i, len(simple), i):  
            simple[j] = False  
 
numbers = numbers[1:] # исключим двойку, ведь число вида (p**6) * (2**x) при p=2  
# не имеет нечетных делителей, кроме 1  
 
for number in numbers:  
    x = 0  
    while number**6 * 2**x <= right: # переберем все варианты 2**x  
        if left <= number**6 * 2**x <= right:  
            ans += 1  
        x += 1  
 
print(ans)  