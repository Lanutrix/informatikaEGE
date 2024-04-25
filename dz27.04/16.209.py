def f(n):
    if n==1:
        return 6
    return 3*n +2 +f(n-1)
def ff(n):
    d = 0
    for j in range(2,n+1):
        d+=3*j
    return 6 + 2*(n-1) + d

# for i in range(1,721):
#     if f(i) != ff(i):
#         print(i)
#         break
#     # print(i,f(i), ff(i))
print(ff(2024)-ff(2020))