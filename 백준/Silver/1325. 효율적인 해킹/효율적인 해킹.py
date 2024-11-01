import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
res = []

for i in range(m):
    a,b = map(int,input().split()) #a가 b를 신뢰한다=b에 a를 넣기
    graph[b].append(a)

def bfs(node):
    q = deque([node])
    cnt = 0
    visited = [False]*(n+1)
    visited[node] = True #함 수 내부에 있어야 초기화 가능
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1
    return cnt

cnt_max = 0
for i in range(1,n+1):
    cnt = bfs(i) #cnt 선언 안 하면 bfs 계속 호출
    if cnt > cnt_max:
        res = [i]
        cnt_max = cnt
    elif cnt_max == cnt:
        res.append(i)

print(*res)