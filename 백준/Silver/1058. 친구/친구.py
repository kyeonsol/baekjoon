import sys
input = sys.stdin.readline

n = int(input())
graph = [[0]*(n) for i in range(n)]
lst = []

for i in range(n):
    lst.append(list(input().rstrip()))

for i in range(n):
    for a in range(n):
        for b in range(n):
            if a==b:
                continue
            if lst[a][b] == 'Y' or (lst[a][i] == 'Y' and lst[i][b] == 'Y'):
                graph[a][b] = 1

ans = 0

for i in graph:
    ans = max(ans, sum(i))

print(ans)