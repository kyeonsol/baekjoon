n,m= map(int,input().split())
lst=[]

for x in range(n+1):
    lst.append(x)

for a in range(m):
    i,j= map(int,input().split())
    lst[i:j+1]= lst[i:j+1][::-1]

print(*lst[1:])