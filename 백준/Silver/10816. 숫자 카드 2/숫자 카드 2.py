import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

m = int(input())
lst2 = list(map(int,input().split()))
cnt = {}

for i in lst:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in lst2:
    if i in cnt:
        print(cnt[i],end=' ')
    else:
        print(0, end=' ')