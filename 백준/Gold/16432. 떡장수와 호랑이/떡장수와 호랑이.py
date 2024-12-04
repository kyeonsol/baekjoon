import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(now,past,lst):
    global visit

    if now == n:
        for i in range(n):
            print(lst[i])
        exit(0)
    
    for i in ddeok[now]:
        if visit[now][i] == False:
            if i != past:
                visit[now][i] = True
                dfs((now+1), i, (lst+[i]))

n = int(input())
ddeok = []
visit = [[False for i in range(10)] for j in range(n)]
#떡 종류 10개

for i in range(n):
    ddeok.append(list(map(int,input().split()))[1:])

dfs(0,0,[])

print(-1)
