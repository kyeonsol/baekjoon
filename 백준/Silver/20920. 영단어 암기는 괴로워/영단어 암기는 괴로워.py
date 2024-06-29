import sys
input = sys.stdin.readline

#자주
#길수록
#사전 순

n, m = map(int,input().split())
lst = {}

for i in range(n):
    a = input().rstrip()

    if len(a) < m: #m 이상의 단어만
        continue
    else:
        if a in lst:
            lst[a] += 1
        else:
            lst[a] = 1

lst = sorted(lst.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in range(len(lst)):
    print(lst[i][0])