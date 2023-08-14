import sys
input = sys.stdin.readline
import math

n = int(input())
a = int(input())
lst = []

for i in range(n-1):
    num = int(input())
    lst.append(num - a)
    a = num

gap = lst[0]
for i in range(1,len(lst)):
    gap = math.gcd(gap,lst[i])

cnt = 0
for i in lst:
    cnt += i // gap - 1

print(cnt)