def find(country, sity):
    if b[country].count(sity) != 0:
        d.append(country)


a = int(input())
b = {}
for i in range(0, a):
    d = []
    c = input().split(" ")
    for k in c[1:]:
        d.append(k)
    b[c[0]] = d
a = int(input())
d = []
for i in range(0, a):
    c = input()
    for k in list(b.keys()):
        find(k, c)
for i in d:
    print(i)