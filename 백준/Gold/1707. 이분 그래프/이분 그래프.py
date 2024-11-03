from collections import deque
import sys

input = sys.stdin.readline

def bfs(node):
    q = deque([node])
    visited[node] = True
    while q:
        v = q.popleft()
        for k in g[v]:
            if not visited[k]:
                q.append(k)
                visited[k] = -visited[v]
            elif visited[k] == visited[v]:
                return False
    return True

k = int(input())

for i in range(k):
    v, e = map(int, input().split())
    g = [[] for i in range(v + 1)]
    visited = [0] * (v + 1)
    res = True

    for j in range(e):
        u1, u2 = map(int, input().split())
        g[u1].append(u2)
        g[u2].append(u1)
    
    for l in range(1, v + 1):
        if not visited[l]:
            if not bfs(l):
                res = False
                break

    print('YES' if res else 'NO')
