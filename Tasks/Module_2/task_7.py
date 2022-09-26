a=int(input('Введите год: '))
a1=a//100
a2=a%100
if a2!=0:
    a1=a1+1
    print(f'Век {a} года: {a1}')
else:
    print(f'Век {a} года: {a1}')