from functools import lru_cache

def moves(h):
    a, b, c, d = h
    return (a + 2, b, c, d), (a, b + 2, c, d), (a, b, c + 2, d), (a, b, c, d + 2), (a * 3, b, c, d), (a, b * 3, c, d), (a, b, c * 3, d), (a, b, c, d * 3)  

@lru_cache(None)
def f(h):
    if sum(h) >= 70:
        return "END"
    if any((f(x) == "END") for x in moves(h)):
        return "P1"
    if all((f(x) == "P1") for x in moves(h)):
        return "V1"
    if any((f(x) == "V1") for x in moves(h)):
        return "P2"
    if all((f(x) == "P2" or f(x) == "P1") for x in moves(h)):
        return "V2"

for s in range(39, 0, -1):
    h = 9, 6, 8, s
    if f(h) == "V2":
        print(s, "V2")
