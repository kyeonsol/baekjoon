import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

for i in range(1,500):
    for j in range(1,500):
        if i**2 + n == j**2:
            cnt += 1

print(cnt)