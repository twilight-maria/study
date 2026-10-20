a=int(input())
b=0
while a>0:
    d=a%10
    if a%2==0:
        b+=1
    a//=10
print(b)