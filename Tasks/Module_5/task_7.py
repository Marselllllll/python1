def fibo(f):
    lst = [1]
    a = 0
    b = 1
    i = 1
    while i < f:
        c = a
        a = b
        b = b + c
        i += 1
        lst.append(b)
    print(b)

fibo(6)