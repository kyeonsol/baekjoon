import sys
input = sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
    a = input()
    if a not in lst:
        lst.append(a)

lst.sort()
lst.sort(key=len)

for i in lst:
    print(i,end='')