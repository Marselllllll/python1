# 4 5 6 0 1 2 3 4 5 6  0  1  2  3
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14
a=int(input('Введите день: '))
a1=a%7
if a1==0:
    print(3)
elif a1==1:
    print(4)
elif a1==2:
    print(5)
elif a1==3:
    print(6)
elif a1==4:
    print(0)
elif a1==5:
    print(1)
elif a1==6:
    print(2)

