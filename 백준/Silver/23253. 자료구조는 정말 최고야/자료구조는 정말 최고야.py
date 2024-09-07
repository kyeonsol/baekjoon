import sys
input = sys.stdin.readline


n,m = map(int,input().split())
flag = True

for i in range(m):
    k = int(input())
    lst = list(map(int,input().split()))
    for j in range(k-1):
        if lst[j]<lst[j+1]:
            flag = False
            break

if flag == False:
    print('No')
else:
    print('Yes')