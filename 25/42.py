a, b = 4202865, 4202924
nums=0
for i in range(a, b):
    f = 1
    for j in range(2, int(i**0.5)):
        if i%j == 0:
            f = 0
            break
    if f:
        nums += 1
        print(nums, i)
