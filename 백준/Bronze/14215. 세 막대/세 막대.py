import sys
input = sys.stdin.readline

lst = list(map(int,input().split()))
lst.sort()

if lst[0] + lst[1] <= lst[2]:
    lst[2] = lst[0] + lst[1] - 1
    print(sum(lst))
else:
    print(sum(lst))