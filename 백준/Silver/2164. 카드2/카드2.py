import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
lst = deque([i for i in range(1,n+1)])

while len(lst) > 1:
    lst.popleft()
    lst.rotate(-1)

print(*lst)