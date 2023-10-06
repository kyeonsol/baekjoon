import sys
input = sys.stdin.readline

n = int(input())

plug = int(input())

for i in range(n-1):
    a = int(input())
    plug += a-1

print(plug)