import sys
input = sys.stdin.readline

v = int(input())
lst = input().strip()
a = 0
b = 0

for i in lst:
    if i == 'A':
        a += 1
    else:
        b += 1

if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print("Tie")