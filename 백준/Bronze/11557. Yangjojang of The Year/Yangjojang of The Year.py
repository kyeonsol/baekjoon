import sys
input = sys.stdin.readline

t = int(input())
lst = []

for i in range(t):
    n = int(input())
    for j in range(n):    
        s, l = input().split()
        s = s.strip()
        l = int(l)
        lst.append([s,l])
    lst = sorted(lst, key = lambda x: x[1])
    print(lst[-1][0])