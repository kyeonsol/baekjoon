import sys
input = sys.stdin.readline

n = int(input())
lst = list((input().rstrip()))
t = 0

for i in lst:
    t += int(i)

print(t)