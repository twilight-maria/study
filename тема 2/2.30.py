a=int(input())
b=int(input())
c=int(input())
if a==b and b==c:
    print('равносторонний')
elif a==b or b==c or a==c:
    print('равнобредренный')
else:
    print('разносторонний')