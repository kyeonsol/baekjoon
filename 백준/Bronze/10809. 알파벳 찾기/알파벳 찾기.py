import sys
input = sys.stdin.readline

s = input().rstrip()
a = 'abcdefghijklmnopqrstuvwxyz'

for i in a:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1,end=' ')