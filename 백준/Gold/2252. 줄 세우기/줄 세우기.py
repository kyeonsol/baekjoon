import sys
input = sys.stdin.readline
from collections import deque
#a가 b보다 반드시 앞에 와야 해서 a->b를 만족 == 전형적 위상정렬

n,m = map(int,input().split())
indegree = [0]*(n+1)
graph = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    res = []
    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        res.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in res:
        print(i,sep=' ')

topology_sort()