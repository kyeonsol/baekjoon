import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(set(map(int,input().split())))
print(*lst)
