a=int(input())
b=0
for i in range(a):
    c=int(input())
    if c>10 and c<100 and c%5 == 0:
        b+=1
print(b)