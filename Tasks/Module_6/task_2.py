lst = [int(a) for a in input().split()]
for i in range(1,len(lst)):
    if lst[i] > lst[i-1]:
        print(lst[i], end=' ')