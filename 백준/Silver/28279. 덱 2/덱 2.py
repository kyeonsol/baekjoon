import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
deque = deque()

for i in range(n):
    a = list(map(int,input().split()))

    if a[0] == 1:
        deque.appendleft(a[1])

    elif a[0] == 2:
        deque.append(a[1])

    elif a[0] == 3:
        if len(deque) != 0:
            print(deque.popleft())
        else:
            print(-1)

    elif a[0] == 4:
        if len(deque) != 0:
            print(deque.pop())
        else:
            print(-1)

    elif a[0] == 5:
        print(len(deque))

    elif a[0] == 6:
        if len(deque) != 0:
            print(0)
        else:
            print(1)

    elif a[0] == 7:
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)

    elif a[0] == 8:
        if len(deque) != 0:
            print(deque[-1])
        else:
            print(-1)