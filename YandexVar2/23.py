def f(a):
    if a==3:
        return 1
    if a<3:
        return 0
    return f(a//3)+f(a - (1 if a%3==0 else a%3))

print(f(58))