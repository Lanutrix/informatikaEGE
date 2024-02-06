from functools import lru_cache

@lru_cache
def ntd(n):
    mxd = 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            mxd = n//i
            break
    return mxd

@lru_cache
def prime_num(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for n in range(170_000,180_001):
    d = ntd(n)
    if int(d**0.5)==d**0.5 and d!=0:
        if prime_num(d):
            print(n//d, d)

print(1)