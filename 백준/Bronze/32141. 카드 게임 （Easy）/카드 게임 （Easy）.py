import sys
input = sys.stdin.readline
#최대한 늦게 죽이기 = 최대한 많은 카드를 사용하기
n,h = map(int,input().split()) #카드의 수, 체력

lst = list(map(int,input().split())) #공격력
cnt = 0

for i in range(n):
    if h<=0:
        break
    h -= lst[i]
    cnt += 1

if h <= 0:
    print(cnt)
else:
    print(-1)