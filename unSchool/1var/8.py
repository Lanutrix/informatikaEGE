import itertools
k = 0
for s in itertools.permutations('ОЛЬГА'):
    if s[0] != 'Ь' and s[s.index("Ь")-1] != "А" and s[s.index("Ь")-1] != "О":
        k+=1

print(k)