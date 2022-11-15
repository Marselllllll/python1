lst = [int(a) for a in input().split()]
lst1 = []
if len(lst) % 2 == 0:
    for i in range(0, len(lst), 2):
        for j in range(1, -1, -1):
            lst1.append(lst[i + j])
else:
    m = lst[len(lst)-1]
    lst.pop(len(lst)-1)
    for i in range(0, len(lst), 2):
        for j in range(1, -1, -1):
            lst1.append(lst[i+j])
    lst1.append(m)

print(lst1)