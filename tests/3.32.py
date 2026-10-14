a=int(input())
for i in range(1,a+1):
    if a%7==0 and a%10==3:
        print(i)
        break
    else:
        print('не найдено')
        break