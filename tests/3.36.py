a=int(input())
b=0
for i in range(a):
    c=int(input())
    if c<=0 or c%4!=0:
        continue
    b+=c
print(b)