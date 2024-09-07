import sys
input = sys.stdin.readline

#다같으면 승리 x

a,b,c = input().split()

if a==b and b==c:
    print('*')

elif a==b:
    print('C')

elif b==c:
    print('A')

else:
    print('B')