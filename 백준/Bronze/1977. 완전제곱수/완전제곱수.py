import sys
input = sys.stdin.readline

m = int(input())
n = int(input())
lst = []

for i in range(m,n+1):
    t = int(i**0.5) ** 2
    if i == t:
        lst.append(i)

if len(lst) > 0:
    print(sum(lst))
    print(lst[0])
else:
    print(-1)