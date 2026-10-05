a=int(input())
if a == 'admin':
    b=int(input())
    if b == '12345':
        print('Добро пожаловать')
    else:
        print('неверный пароль')
else:
    print('неверный логин')
