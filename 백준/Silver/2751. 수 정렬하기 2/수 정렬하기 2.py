import sys
input = sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
    a = int(input())
    lst.append(a)

lst.sort()

print(*lst,sep='\n')