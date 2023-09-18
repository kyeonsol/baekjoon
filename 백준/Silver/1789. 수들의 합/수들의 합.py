import sys
input = sys.stdin.readline

s = int(input())
cnt = 0
result = 0

for i in range(1,s+1):
    cnt += 1
    result += i
    if result > s:
        cnt -= 1
        break
    
print(cnt)