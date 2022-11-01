a, b, c = map(int, input('Введите три числа через пробел: ').split())
n = [a, b, c]
aa = n.count(a)
bb = n.count(b)
cc = n.count(c)
if max(aa, bb, cc) == 1:
    print(0)
else:
    print(max(aa, bb, cc))