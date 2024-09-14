import sys
input = sys.stdin.readline

n,x = map(int,input().split()) #number of viewpoints, maximum meters
lst = list(map(int,input().split())) #non-decreasing
cnt = 1
res = []

for i in range(n-1):
    if lst[i+1]-lst[i] <= x:
        cnt += 1
    
    else:
        res.append(cnt)
        cnt = 1
res.append(cnt)

print(max(res))