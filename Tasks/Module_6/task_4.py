lst = [int(a) for a in input().split()]
mx = 0
mn = 10**100
for i in lst:
    mx = max(mx, i)
    mn = min(mn, i)
mxx = lst.index(mx)
mnn = lst.index(mn)
lst.pop(mxx)
lst.insert(mxx, mn)
lst.pop(mnn)
lst.insert(mnn, mx)
print(lst)