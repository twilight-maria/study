a=int(input())
b=0
for i in range(a):
    c=int(input())
    if c>=0 and c%4!=0:
        continue
    c+=1
print(b)