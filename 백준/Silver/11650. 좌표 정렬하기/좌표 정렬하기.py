import sys
input = sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
    a,b = map(int,input().split())
    lst.append([a,b])

lst.sort(key = lambda x : (x[0],x[1]))

for i in range(n):
    print(*lst[i],end='\n')