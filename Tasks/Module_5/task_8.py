a = 1
mx = 0
lst = []
while a != 0:
    a = int(input())
    lst.append(a)
for i in lst:
    mx = max(mx, lst.count(i))
print(mx)