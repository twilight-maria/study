secret=37
while True:
    a=int(input())
    if a==secret:
        print('угадал')
        break
    elif a<secret:
        print('больше')
    else:
        print('меньше')