import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

n = int(input())
tree = [[] for i in range(n+1)]
parent = [0 for i in range(n+1)]
dep = [0 for i in range(n+1)]
cnt = [False]*(n+1)

#깊이 구하기
def dfs(x, depth):
    cnt[x] = True
    dep[x] = depth
    for j in tree[x]:
        if cnt[j]:
            continue
        parent[j] = x
        dfs(j, depth+1)

#최소 공통 조상 찾기
def lca(a,b):
    while dep[a] != dep[b]: #깊이 동일
        if dep[a] > dep[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b: #노드 동일
        a = parent[a]
        b = parent[b]
    return a

#양방향 저장
for i in range(n-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

#루트 노드는 1번
dfs(1,0) 

m = int(input())

for i in range(m):
    x, y = map(int,input().split())
    print(lca(x,y))