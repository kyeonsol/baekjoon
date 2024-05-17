import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
lst = deque([])

for i in range(n):
    a = input().split() #index = 0~1
    if a[0] == 'push':
        lst.append(a[1])
    elif a[0] == 'pop':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[0])
            lst.popleft()
    elif a[0] == 'size':
        print(len(lst))
    elif a[0] == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(lst) == 0:
           print(-1)
        else:
           print(lst[0])
    elif a[0] == 'back':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])