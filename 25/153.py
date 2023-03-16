a = 1
mn = float('inf')
for a2 in range(1, 26):
    for a3 in range(1, 26):
        for a5 in range(1, 6):
            for a7 in range(1, 6):
                for a11 in range(1, 6):
                    for a13 in range(1, 6):
                        for a17 in range(1, 6):
                            for a19 in range(1, 6):
                                if a2*a3*a5*a7*a11*a13*a17*a19 == 1600:
                                    n = 2**(a2-1) * 3**(a3-1) * 5**(a5-1)\
                                        * 7**(a7-1) * 11**(a11-1) * 13**(a13-1)\
                                        * 17**(a17-1) * 19**(a19-1)
                                    if n < mn:
                                        mn = n

print(mn, 19)