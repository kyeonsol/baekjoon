import sys
input = sys.stdin.readline

num = []

for i in range(2,246913):
    cnt = 0
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            cnt += 1
            break
    if cnt == 0:
        num.append(i)

while 1:
    n = int(input())
    res = 0
    if n == 0:
        break
    for i in num:
        if n < i <= 2*n:
            res += 1
    print(res)