def operation(full, shot):
    if c[0] == full:
        if b[c[1]].count(shot) != 0:
            v.append("OK")
        else:
            v.append("Denied")


a = int(input())
b = {}
for i in range(0, a):
    v = []
    c = input().split(" ")
    for k in c[1:]:
        v.append(k)
    b[c[0]] = v

a = int(input())
v = []
for i in range(0, a):
    c = input().split(" ")
    operation('read', 'R')
    operation('write', 'W')
    operation('execute', 'X')
for i in v:
    print(i)
