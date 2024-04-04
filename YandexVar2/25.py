s = [str(i) for i in range(10)]
count, mx = 0, 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                g = int(f'4{a}8{b}15{c}16{d}23')
                if g%123==42:
                    count+=1
                    mx = max(mx, g)

print(count, mx)