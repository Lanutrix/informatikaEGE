f = [1] * 2030

for n in range(2, 2030):
    f[n] = n * f[n-1]

print(f[2023]/f[2020])