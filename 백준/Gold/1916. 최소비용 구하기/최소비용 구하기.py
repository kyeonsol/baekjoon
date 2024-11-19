import sys
input = sys.stdin.readline
import heapq

INF = int(1e9)
n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for i in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

a,b = map(int,input().split())

def dijstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            if dist+i[1] < distance[i[0]]:
                distance[i[0]] = dist+i[1]
                heapq.heappush(q, (dist+i[1], i[0]))

dijstra(a)
print(distance[b])