import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
score = 0
scs = 1

for i in range(n):
    if lst[i] == 1:
        score += scs
        scs += 1
    else:
        scs = 1
        
        
print(score)