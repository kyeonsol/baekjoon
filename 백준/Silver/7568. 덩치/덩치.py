import sys
input = sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
    x, y = map(int,input().split())
    lst.append([x,y])

cnt = 0

for i in range(n):
    cnt = 0
    fir = lst[i]
    for j in range(n):
        if i == j :
            continue
        if fir[0] < lst[j][0] and fir[1] < lst[j][1]:
            cnt += 1
    print(cnt+1,end=' ')