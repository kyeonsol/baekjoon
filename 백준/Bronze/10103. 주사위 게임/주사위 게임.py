import sys
input = sys.stdin.readline

n = int(input())
#낮은 숫자가 나온 사람은 상대편 주사위에 
#나온 숫자만큼 점수를 잃게 된다
#같은 숫자가 나온 경우에는 아무도 점수를 
#잃지 않는다.
cy = 100
sd = 100

for i in range(n):
    a, b = map(int,input().split())
    if a < b:
        cy = cy - b
    elif a > b:
        sd = sd - a
    else:
        continue

print(cy)
print(sd)
