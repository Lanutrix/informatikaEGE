for i in range(100_000_000, 101_000_000 + 1):
    if i % 2 == 0:
        count = 1
        sqrtI = round(i ** 0.5)
        dt = 0
        for j in range(2, sqrtI + 1):
            if i % j == 0:
                if j % 2 == 0:
                    count += 1
                k = i // j
                if k % 2 == 0:
                    if j != k:
                        count += 1
                        dt = j
                if count > 3:
                    break
        if count == 3:
            print(i, dt)
