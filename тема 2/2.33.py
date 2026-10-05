x=int(input())
y=int(input())
if x>0 and y>0:
    print('1 четверть')
elif x<0 and y>0:
    print('2 четверть')
elif x<0 and y<0:
    print('3 четверть')
elif x>0 and y<0:
    print('4 четверть')
elif x == 0 and y == 0:
    print('Начало координат')
elif x == 0:
    print('Ось Y')
else:
    print('Ось X')