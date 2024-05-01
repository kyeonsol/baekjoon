import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

lst_s = sorted(set(lst))

dic = dict()
cnt = 0

for i in lst_s:
    dic[i] = cnt
    cnt += 1

for i in lst:
    print(dic[i], end=' ')