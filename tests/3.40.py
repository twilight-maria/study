a=int(input())
b=1
while a>0:
    d=a%10
    b*=d
    a//=10
print(b)