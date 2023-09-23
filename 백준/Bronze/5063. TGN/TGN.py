import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    r, e, c = map(int,input().split())
    #광고 안 했을 때, 광고 했을 때, 광고 비용
    if r < e-c:
        print("advertise")
    elif r == e-c:
        print("does not matter")
    else:
        print("do not advertise")