import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    p = int(input())
    dic = {}
    for j in range(p):
        a, b = input().split()
        a = int(a)
        dic[a] = b
    print(dic.get(max(dic.keys())))