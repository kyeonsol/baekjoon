import sys
input = sys.stdin.readline

def dfs(now,past,lst):
    global visit #전역 변수 선언

    if now == n: #다 돌았다면
        for i in range(n):
            print(lst[i])
        exit(0) #이후 print(-1)이 실행되지 않도록 exit
    
    for i in ddeok[now]: #
        if visit[now][i] == False:
            if i != past:
                visit[now][i] = True
                dfs((now+1), i, (lst+[i]))

n = int(input())
ddeok = [] #떡 종류 정보 저장
visit = [[False for i in range(10)] for j in range(n)] #떡 종류 10개

for i in range(n):
    ddeok.append(list(map(int,input().split()))[1:]) #개수 제외하고 저장

dfs(0,0,[]) #첫날은 past가 없음

print(-1) #떡을 줄 방법이 없다면
