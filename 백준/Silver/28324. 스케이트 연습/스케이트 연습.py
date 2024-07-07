import sys
input = sys.stdin.readline

#시작 지점, N개의 중간 지점, 도착 지점
#속력 제한, 높이는 건 무한, 줄이는 건 1만
#출발, 도착 지점 외에서 속력 0은 안됨
#성과 = 각 지점에서 속력의 합 (최대화 필요)

n = int(input())
vlst = list(map(int,input().split()))
vlst.reverse()
vlst[0] = 1
total = vlst[0]

for i in range(1,len(vlst)):
    if vlst[i]-vlst[i-1] > 1:
            total += vlst[i-1]+1
            vlst[i] = vlst[i-1]+1
    else:
        total += vlst[i]

print(total)