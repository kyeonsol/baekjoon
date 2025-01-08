import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for i in range(n+1)]
visit = [False]*(n+1)
ans = [0]*(n+1)

for i in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(num):
    visit[num] = True
    for i in tree[num]:
        if not visit[i]:
            ans[i] = num #부모 노드 지정
            dfs(i)

dfs(1) #루트인 1부터 시작

for i in range(2,n+1):
    print(ans[i])
