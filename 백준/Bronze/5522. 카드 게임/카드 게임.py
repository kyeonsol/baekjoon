import sys
input = sys.stdin.readline

score = 0

for i in range(5):
    a = int(input())
    score += a

print(score)