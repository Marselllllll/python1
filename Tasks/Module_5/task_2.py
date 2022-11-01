a = int(input('Ввердите число: '))
n = 0
while 2**n <= a:
    n += 1
print(n-1, 2**(n-1))