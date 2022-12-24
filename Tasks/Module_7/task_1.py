a = input("Введите слова через пробел: ")
b = []
a = a.split(" ")
for i in range(0, len(a)):
    b.append(a[:i].count(a[i]))
print(a)
print(b)
