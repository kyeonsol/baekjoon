import sys
input = sys.stdin.readline

t = int(input())

#A = 5분 = 300초, B = 1분 = 60초, C = 10초
#t는 초단위, 최소 버튼 조작

if t % 10 != 0:
    print(-1)
else:
    a, b, c = 0, 0, 0
    a = t // 300
    b = (t % 300) // 60
    c = (t % 60) // 10
    print(a, b, c)