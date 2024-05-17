import sys
input = sys.stdin.readline
from collections import deque

n,k = map(int,input().split())
nlst = list(range(1,n+1))
lst = deque(nlst) #generate circle
res = []

for i in range(n):
    lst.rotate(-(k-1))
    res.append(lst.popleft()) #pop 3rd num

print('<',end='')
print(*res,sep=', ',end='')
print('>')

