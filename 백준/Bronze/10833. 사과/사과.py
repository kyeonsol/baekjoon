import sys
input = sys.stdin.readline

n = int(input())
total = 0

for i in range(n):
    student, apple = map(int,input().split())
    total += apple % student

print(total)