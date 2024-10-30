from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(node):
    ans = []
    q = deque([node])
    visited[node] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]: #False이면 True가 되어 실행 (방문하지 않은 인접노드 삽입)
                q.append(i)
                visited[i] = True
                distance[i] = distance[v]+1
                if distance[i] == k:
                    ans.append(i)
    if len(ans) == 0:
        print(-1)
    else:
        ans.sort()
        for i in range(len(ans)):
            print(ans[i],end='\n')


bfs(x)