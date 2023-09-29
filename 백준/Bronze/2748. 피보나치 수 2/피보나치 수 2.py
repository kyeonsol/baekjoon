import sys
input = sys.stdin.readline

lst = [0,1]
n = int(input())

for i in range(n-1):
    lst.append(lst[i]+lst[i+1])

print(lst[-1])