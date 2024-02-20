# cnt = 0
# ht = []
# for i1 in range(10):
#     for i2 in range(10):
#         if i1%2==0 and i2%2==0:
#             ht.append(f'{i1}{i2}')
#         if i1%2!=0 and i2%2!=0:
#             ht.append(f'{i1}{i2}')
# # print(ht,nh)
# for i in range(262144, 2097152):
#     s = oct(i)[2:]
#     if len(set(s))==7:
#         f = 1
#         for k in ht:
#             if k in s:
#                 f=0
#                 break
#         if f:
#             cnt+=1

# print(cnt)
c = 0
for i in range(1,16):
    c+=i

print(c/16)
print(17/2)