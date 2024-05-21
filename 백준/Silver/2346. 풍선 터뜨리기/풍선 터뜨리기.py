import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
b = deque(list(map(int,input().split())))
index = deque([i for i in range(1,n+1)])
res = []

for i in range(n):
    a = b.popleft()
    res.append(index.popleft())
    if a>0:
        b.rotate(-a+1)
        index.rotate(-a+1)
    else:
        b.rotate(-a)
        index.rotate(-a)

print(*res)