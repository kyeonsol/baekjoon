import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

dp = [0]*n

for i in range(1,n):
    if lst[i] > lst[i-1]:
        dp[i] = dp[i-1] + 1
print(sum(dp)+n)