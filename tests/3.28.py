a=int(input())
b=int(input())
for i in range (a):
    c=int(input())
    if c>=0 and c%2==0 and c%5!=0:
        b+=c
print(a)