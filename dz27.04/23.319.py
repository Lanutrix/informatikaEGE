def way(n):
    c = [1,3,5]
    sm = [0] * (n+1)
    sm[0] = 1
    for coin in c:
        for i in range(coin, n+1):
            sm[i] += sm[i - coin]
    return sm[n]
ways = way(112500)
ans = sum(int(x) for x in str(ways))
print(ans,ways)
