import sys
input = sys.stdin.readline

n, x = map(int,input().split()) #x보다 작은 수
lst = list(map(int,input().split()))
res = []

for i in range(n):
    if lst[i] < x:
        res.append(lst[i])

print(*res)