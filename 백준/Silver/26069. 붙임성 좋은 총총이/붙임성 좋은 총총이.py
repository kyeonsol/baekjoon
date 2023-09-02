import sys
input = sys.stdin.readline

n = int(input())
set = {'ChongChong'}

for i in range(n):
    a,b = input().strip().split()

    if a in set:
        set.add(b)

    if b in set:
        set.add(a)

print(len(set))