a = int(input("Введите количество пар: "))
b = {}
print("Вводите попарно слова синонимы:\n")
for i in range(0, a):
    c = input().split(" ")
    b[c[0]] = c[1]
d = input("\nВведите ключ: ")
print(f"Синоним: {b.get(d)}")
