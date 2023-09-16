import sys
input = sys.stdin.readline

a, b, c = map(int,input().split())
d = int(input())

x = d // 60
y = d % 60

b = x + b
c = y + c

while c >= 60:
    b = b+1
    c = c - 60

while b >= 60:
    a = a+1
    b = b - 60

while a >= 24:
    a = a - 24

print(a,b,c,sep=" ")