# (x ≡ ( w ∨ y)) ∨ ((w → z ) ∧ (y → w))

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # ((x ∧ w) ∨ (w ∧ z)) ≡ ((z → y) ∧ (y → x)).
                if (((x*w) + (w*z)) == ((z<=y) * (y<=x))):
                    print(x, y, z, w)