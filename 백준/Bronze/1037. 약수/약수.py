import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

if n == 1:
    print(max(lst)**2)
else:
    print(max(lst)*min(lst))