a=int(input())
if (100<= a <=999) and (a % 2 == 0) and (a % 10 != 0) and (a % 3 == 0 or a % 7 == 0):
    print('YES')
else:
    print('NO')