alf  = 'sgsgssgsg'  # 'ГИПЕРБОЛА'
alfs = 'ggggg'      # 'ГПРБЛ'

cnt = 0

for a in alfs:
    for b in alf:
        for c in alf:
            for d in alf:
                for e in alf:
                    for f in alfs:
                        s = a+b+c+d+e+f
                        if not('gsg' in s):
                            cnt+=1
print(cnt)


# alf  = 'ГИПЕРБОЛА'#'sgsgssgsg'  #
# # alfs = 'ggggg'      # 'ГПРБЛ'
# g = 'ГПРБЛ'
# sog = "ИЕОА"
# cnt = 0

# for a in alf:
#     for b in alf:
#         for c in alf:
#             for d in alf:
#                 for e in alf:
#                     for f in alf:
#                         s = list(a+b+c+d+e+f)
#                         lol = 1
#                         for i in range(4):
#                             if (s[i] in g) and (s[i+1] in sog) and (s[i+2] in g):
#                                 lol = 0
#                                 break
#                         if lol:
#                             cnt+=1
# print(cnt)


# # cnt = 0

# # for a in 'gs':
# #     for b in 'gs':
# #         for c in 'gs':
# #             for d in 'gs':
# #                 s = a+b+c+d
# #                 if not(a=='g' and b=='s') and not('gsg' in s):
# #                     f = list(map(int, list(s.replace('g','4').replace('s','5'))))
# #                     k = 25
# #                     for i in f:
# #                         k *= i
# #                     cnt+=k
# # print(cnt)