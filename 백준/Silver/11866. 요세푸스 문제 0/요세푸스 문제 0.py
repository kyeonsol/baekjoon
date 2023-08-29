import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int,input().split())
lst = deque([i for i in range(1,n+1)])
result = []

while len(lst) != 0:
    for i in range(k-1):
        lst.append(lst.popleft())
    result.append(lst.popleft())

print('<', end='')
print(*result, sep=', ', end='')
print('>', end='')