import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    a = int(input())
    print(a**2)
else:
    lst = list(map(int,input().split()))
    slst = sorted(lst)
    print(slst[0]*slst[-1])