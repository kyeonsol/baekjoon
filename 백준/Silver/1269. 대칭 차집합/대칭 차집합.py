import sys
input = sys.stdin.readline

a,b = map(int,input().split())
lsta = set(map(int,input().split()))
lstb = set(map(int,input().split()))

print(len(lsta-lstb) + len(lstb-lsta))