n,m= map(int,input().split())
lst= [0]*(n+1)

for a in range(m):
    i,j,k= map(int,input().split())
    for b in range(i,j+1):
        lst[b]= k

print(*lst[1:])