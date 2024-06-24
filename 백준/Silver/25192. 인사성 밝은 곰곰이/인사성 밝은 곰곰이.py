import sys
input = sys.stdin.readline

cnt = 0

n = int(input())

for i in range(n):
    a = input().rstrip()
    if a == 'ENTER':
        s = set()
    elif a not in s:
        s.add(a)
        cnt += 1

print(cnt)
