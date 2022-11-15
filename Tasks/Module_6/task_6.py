lst1 = [int(a) for a in input().split()]
lst2 = [int(b) for b in input().split()]
lst =[]
for i in lst1:
    if lst2.count(i) != 0:
        if lst.count(i) == 0:
            lst.append(i)
[print(j, end=' ') for j in lst]