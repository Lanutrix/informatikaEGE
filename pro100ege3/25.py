# 1A2157B4
def nez(n):
    ns = [1 for i in str(n) if int(i)%2!=0]
    return len(ns)== len(str(n))

bb = [''] + [f'{i:>01}' for i in range(10) if nez(i)] + [f'{i:>02}' for i in range(100) if nez(i)] + [f'{i:>03}' for i in range(1000) if nez(i)]

l = []
for a in ["0", "2", "4", "6", "8"]:
    for b in bb:
        cc = int(f"1{a}2157{b}4")
        if cc<=10**10:
            if cc%133==0:
                l.append(cc)

l = sorted(l)

for i in l:
    print(i, i//133)