a = int(input("Введите число: "))
n = 1
v = []
while n**2 <= a:
    n += 1
    v.append(n**2)
for i in v[:-1]:
    print(i)