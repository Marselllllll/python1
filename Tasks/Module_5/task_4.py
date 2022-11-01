a = -1
n = -1
b = 0
while a != 0:
    a = int(input())
    if a > b:
        n += 1
        b = a
print(n)
