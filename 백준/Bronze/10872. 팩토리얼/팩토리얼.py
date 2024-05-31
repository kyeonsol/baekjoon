import sys
input = sys.stdin.readline

n = int(input())
m = 1

for i in range(2,n+1):
    m *= i

print(m)