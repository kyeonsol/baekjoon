import sys
input = sys.stdin.readline

n = int(input())
s = set()
ans = 0

for i in range(n):
    a = input().strip()
    if a == 'ENTER':
        s.clear()
        ans += len(s)
    elif a not in s:
        ans += 1
        s.add(a)

print(ans)