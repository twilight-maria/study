a=int(input())
b=0
while a>0:
    d=a%10
    b=b*10+d
    a//=10
print(b)