import sys
input = sys.stdin.readline

n = int(input())
lst = set(map(int,input().split()))
m = int(input())
lst2 = list(map(int,input().split()))

for i in range(m):
    if lst2[i] in lst:
        print(1,end=' ')
    else:
        print(0,end=' ')
