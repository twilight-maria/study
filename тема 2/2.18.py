a=int(input())
if 0 <= a <=6:
    print('дошкольный')
elif 7 <= a <= 17:
    print('школьный')
elif 18 <= a <= 64:
    print('взрослый')
else:
    print('Пенсионер')