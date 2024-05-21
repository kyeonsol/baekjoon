import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
paper = deque(list(map(int, input().split())))
index = deque([i for i in range(1, n + 1)])
poped = []

while paper:
    num = paper.popleft()
    poped.append(index.popleft())
    if num > 0:
        paper.rotate(-(num-1))
        index.rotate(-(num-1))
    else:
        paper.rotate(-num)
        index.rotate(-num)
print(*poped)