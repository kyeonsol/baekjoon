import sys
input = sys.stdin.readline

date = int(input())
lst = list(map(int,input().split()))
cnt = 0

for i in range(5):
    if lst[i] == date:
        cnt += 1
        
print(cnt)