def fibo(f):
    lst = [1]
    a = 0
    b = 1
    while b < f:
        c = a
        a = b
        b = b + c
        lst.append(b)
    if b == f:
        if f == 1:
            print(1)
        else:
            print(len(lst))
    else:
        print(-1)

fibo(8)