# def f(n):
#     if n<=1:
#         return 0.5
#     return (n+1)*f(n-1)

# print(f(14)/f(4))
# c = 0
# s = 0.5
# for n in range(2,15):
#     s *= n+1
#     if n==4:
#         c = s
# print(s/c)

# c = 0
# s = 0.5
# for n in range(5,15):
#     s *= n+1
# print(s)
s = 1
for i in range(199,201):
    s*=(i+1)

print(s)