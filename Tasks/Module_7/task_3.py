a = int(input())
b = {}
c = []
for i in range(0, a):
    d = input().split(" ")
    c.append([d[0], int(d[1])])
c.sort()
for i in c:
    if b.get(i[0]) == None:
        b[i[0]] = i[1]
    else:
        b[i[0]] = b[i[0]] + i[1]
for i in b:
    print(i, b[i])