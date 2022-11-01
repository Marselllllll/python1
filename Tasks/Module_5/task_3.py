a, b = map(int, input('Введите дистацию первой и необходимой пробежки чрезе пробел: ').split())
n = 1
sum = a
while sum <= b:
    a += a/10
    sum += a
    n += 1
print(n)
