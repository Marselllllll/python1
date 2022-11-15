lst = [int(a) for a in input().split()]
lst1 = []
for i in lst:
    if lst1.count(i) == 0:
        lst1.append(i)
        print('НЕТ')
    else:
        print('ДА')