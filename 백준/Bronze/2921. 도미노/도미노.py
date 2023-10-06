import sys
input = sys.stdin.readline

n = int(input())
lst = 3

for i in range(2,n+1):
    lst += (i*(i+1)) + (i*(i+1))//2

print(lst)