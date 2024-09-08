import sys
input = sys.stdin.readline

n = int(input())
s = {0}
b = 0

for i in range(1,n+1):
    a = b-i
    if a<0 or a in s:
        a = b+i
    s.add(a)
    b = a

print(b)