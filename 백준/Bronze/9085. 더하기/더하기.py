import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    lst = map(int,input().split())
    print(sum(lst))