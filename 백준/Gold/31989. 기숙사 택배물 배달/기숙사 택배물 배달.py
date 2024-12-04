import sys
input = sys.stdin.readline

n,m = map(int,input().split()) #방은 2n+1개, m개의 택배
store = n #택배보관실
lst = list(map(int,input().split())) #각 방의 입구에서부터의 거리
dis = [0]*(2*n+1)
weight = [0]*(2*n+1)

#택배물 보관실로부터의 거리로 환산
for i in range(2*n+1):
    if i<store:
        dis[i] = lst[store] - lst[i]
    elif i>store:
        dis[i] = lst[i] - lst[store]
    else:
        dis[i] = 0

for i in range(m):
    a,b = map(int,input().split()) #a번 방, 무게 b
    if a != store+1:
        weight[a-1] += b

#택배물 보관실 기준 좌측 시간 구하기
left = sum(weight[:store])
cnt1 = 0
now = store

for i in range(store-1,-1,-1):
    if weight[i] == 0:
        continue
    cnt1 += (dis[i] - dis[now]) * (left+1) #가는 거리
    now = i
    left -= weight[i]

cnt1 += dis[now]

#택배물 보관실 기준 우측 시간 구하기
right = sum(weight[store+1:])
cnt2 = 0
now = n

for i in range(store+1,2*n+1):
    if weight[i] == 0:
        continue
    cnt2 += (dis[i] - dis[now]) * (right+1) #가는 거리
    now = i
    right -= weight[i]

cnt2 += dis[now]

print(cnt1+cnt2)
