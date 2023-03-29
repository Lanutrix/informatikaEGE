number = 2*(216**6) + 3*(36**9) - 432 
k = 0
while number > 0:
        if number % 6 == 5:
            k+=1
        number //= 6
print(k)