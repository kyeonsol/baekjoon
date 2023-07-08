import sys
input = sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
    [a,b] = map(int,input().split())
    lst.append([b,a])

s_lst = sorted(lst)

for i in range(n):
    print(s_lst[i][1],s_lst[i][0])