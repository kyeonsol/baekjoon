import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
deq = deque(enumerate(map(int,input().split()), start = 1))

for i in range(n):
    p = deq.popleft()
    print(p[0], end=' ')
    if p[1] > 0:
        deq.rotate(-(p[1] - 1))
    else:
        deq.rotate(-p[1])
