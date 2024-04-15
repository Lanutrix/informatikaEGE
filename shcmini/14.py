for x in range(14):
    a = int('3A0D11',14)
    b = int('740C8', 14)
    c = int('08A63', 14)
    f = a+b+c+ x*14**3 + x*14**2 + x *14**4

    if f%10==0:
        print(f//10)
        break