import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort(reverse = True)
res = []

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if m < lst[i] + lst[j] + lst[k]:
                continue
            else:
                res.append(lst[i] + lst[j] + lst[k])

print(max(res))