import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

num = str(a*b*c)
cnt = 0

for i in range(10):
    print(num.count(str(cnt)))
    cnt += 1