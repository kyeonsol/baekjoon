import sys
input = sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
    a = int(input())
    if a == 0:
        del lst[-1]
    else:
        lst.append(a)

print(sum(lst))