import sys
input = sys.stdin.readline

n = int(input())
lst = [0,1]

for i in range(n):
    lst.append(lst[i]+lst[i+1])

print(lst[-2])