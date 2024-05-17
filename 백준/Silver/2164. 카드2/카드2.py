import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
lst = list(range(1,n+1))
queue = deque(lst) #card generate

while len(queue) > 1:
    queue.popleft()
    queue.rotate(-1)

print(*queue)