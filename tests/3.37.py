a=int(input())
for i in range(1,a+1):
    b=i%10
    if b==5 or b==0:
        continue
    print(i)