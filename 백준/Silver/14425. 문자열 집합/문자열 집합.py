import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = []
tst = []
cnt = 0

for i in range(n):
    a = input()
    lst.append(a)
    set(lst)

for i in range(m):
    a = input()
    tst.append(a)

for i in range(m):
    if tst[i] in lst:
        cnt += 1
    else:
        pass

print(cnt)