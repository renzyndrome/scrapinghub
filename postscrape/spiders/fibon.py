def fibon(n):
    a = b = 1

    for i in range(n):
        yield a
        a, b = b, a+b

for i in fibon(5):
    print(i)