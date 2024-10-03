import sys
input = sys.stdin.readline

lst = []
r = 0
b = 0

for i in range(8):
    a = input().split()
    a0 = a[0].split(':')
    lst.append([a[1],a0])


lst.sort(key=lambda x : (x[1][0], x[1][1], x[1][2]))


score = [10,8,6,5,4,3,2,1,0]
for i in range(8):
    if lst[i][0] == 'R':
        r += score[i]
    else:
        b += score[i]

if r>b:
    print('Red')
else:
    print('Blue')