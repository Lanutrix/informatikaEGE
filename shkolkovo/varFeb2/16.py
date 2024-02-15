# from functools import lru_cache

# @lru_cache
# def F(n,m):
#     if m>n:
#         return 0
#     if n%m==0:
#         return 19+F(n, m+1)
#     return F(n, m+2)

# print( F(176586,19))



# def F(n, m):
#     result = 0
#     stack = [(n, m)]

#     while stack:
#         n, m = stack.pop()

#         if m > n:
#             continue
#         if n % m == 0:
#             result += 19
#             stack.append((n, m + 1))
#         else:
#             stack.append((n, m + 2))

#     return result

# print(F(176586, 19))



n,m = 176586,19
s = 0
while m<=n:
    if n%m==0:
        s+=19
        m+=1
    else:
        m+=2

print(s)