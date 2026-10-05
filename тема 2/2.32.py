a=int(input())
b=input()
c=int(input())
if b=='+':
    print(a+c)
elif b=='-':
    print(a-c)
elif b=='*':
    print(a*c)
elif b=='/':
    if c==0:
        print('на ноль делить нельзя')
    else:
        print(a/b)