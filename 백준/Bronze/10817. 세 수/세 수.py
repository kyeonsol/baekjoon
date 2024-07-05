import sys
input = sys.stdin.readline

lst = list(map(int,input().split()))

lst.remove(max(lst))
print(max(lst))