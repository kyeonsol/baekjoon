import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst1 = []
lst2 = []

for i in range(n):
    a = list(map(int,input().split()))
    lst1.append(a) #리스트 안에 리스트 m개를 생성

for i in range(n):
    b = list(map(int,input().split()))
    lst2.append(b)

for i in range(n):
    total = []
    for j in range(m):
        total.append(lst1[i][j] + lst2[i][j])
    print(*total)
