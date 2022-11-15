lst1 = [int(a) for a in input().split()]
lst2 = [int(b) for b in input().split()]
c = 0
for i in lst1:
    if lst2.count(i) != 0:
        c += 1
print(c)