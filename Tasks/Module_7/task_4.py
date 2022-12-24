a = int(input())
d = {}
for i in range(0, a):
    b = input().split(" ")
    for k in b:
        if d.get(k) == None:
            d[k] = 1
        else:
            d[k] += 1
c = d.values()
if max(c) == 1:
    m = d.keys()
    print(sorted(m)[0])
else:
    print(list(d.keys())[list(d.values()).index(max(c))])