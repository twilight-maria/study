a=int(input())
b=int(input())
for _ in range(a-1):
    c=int(input())
    if c<b:
        b=c
print(b)