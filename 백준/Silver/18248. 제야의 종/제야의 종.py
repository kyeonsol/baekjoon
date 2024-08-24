import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = []

def ring():
    global n,m
    for i in range(1,n):
        for j in range(m):
            if lst[i-1][0][j] == 1 and lst[i][0][j] == 0:
                return 'NO'
    return 'YES'
    
for i in range(n):
    a = list(map(int,input().split()))
    a_cnt = a.count(1)
    lst.append([a,a_cnt])

lst.sort(key=lambda x:x[1])

print(ring())