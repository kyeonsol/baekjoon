import sys
input = sys.stdin.readline

t = int(input())

for i in range(1,t+1):
    a, b = map(int,input().split())
    score = a + b
    print(f'Case {i}: {score}')
