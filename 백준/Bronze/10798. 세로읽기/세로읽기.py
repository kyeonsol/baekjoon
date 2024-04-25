import sys
input = sys.stdin.readline

lst = []
for i in range(5):
    lst.append(input().rstrip())

max_ = 0
for i in range(len(lst)):
    if max_ < len(lst[i]):
        max_ = len(lst[i])

res = ''
for j in range(max_):
    for i in range(5):
        if j < len(lst[i]):
            res += lst[i][j]

print(res)