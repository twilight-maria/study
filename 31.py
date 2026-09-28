a=int(input())
b=a//1000
c=a//100%10
d=a//10%10
e=a%10
s=b+c+d+e
s1=b*c*d*e
s2=b==e
s3=b+e==c+d
print(b,c,d,e,s,s1,s2,s3)


