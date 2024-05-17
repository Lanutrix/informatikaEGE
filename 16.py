from functools import lru_cache
@lru_cache
def f(n):
    if n<=1:
        return 1
    if n%3==0:
        return f(n-1)+n//3
    return f(n-1)+f(n-2)
print(f(54)-f(52)-f(50))