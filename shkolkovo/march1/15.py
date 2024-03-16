P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
print(P|Q, P&Q)
A = list(P&Q)
P = list(P)
Q = list(Q)

for x in range(-1000, 10000):
    f = 1
    if not(  not( (x not in A) and (x in Q)) or (x not in P)  ):
        f  = 0
print(f)