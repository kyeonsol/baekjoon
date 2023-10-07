import sys
input = sys.stdin.readline

n = int(input())
lst = [0,1]

for i in range(n):
    a = lst[i] + lst[i+1]
    lst.append(a)

print(lst[-2])