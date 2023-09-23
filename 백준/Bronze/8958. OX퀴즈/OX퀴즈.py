import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    lst = list(input())
    cnt = 0
    score = 0
    for j in lst:
        if j == 'O':
            score += 1
            cnt += score
        else:
            score = 0

    print(cnt)
