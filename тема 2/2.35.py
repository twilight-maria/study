a=int(input('месяц'))
b=int(input('день'))
if a<1 or a>12:
    print('такой даты нет')
else:
    if a==2:
        bm=28
    elif a==4 or a==6 or a==9 or a==11:
        bm=30
    else:
        bm=31
    if b<1 or b>bm:
        print('такой даты нет')
    else:
        print('дата существует')
