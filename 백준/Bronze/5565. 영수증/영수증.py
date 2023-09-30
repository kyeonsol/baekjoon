import sys
input = sys.stdin.readline

total = int(input())

for i in range(9):
    a = int(input())
    total -= a

print(total)