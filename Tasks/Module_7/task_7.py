a = int(input())
c = []
d = {}
for i in range(0, a):
    b = input().split(" ")
    for k in b:
        c.append(k)
for i in c:
    d[i] = c.count(i)
m = max(list(d.values()))
for i in range(m, 0, -1):
    for k in d:
        if d[k] == i:
            print(k, d[k])
