n,m= map(int,input().split())
lst=[]

for i in range(n+1):
    lst.append(i)

for a in range(m):
    i,j= map(int,input().split())
    lst[i],lst[j]=lst[j],lst[i]

print(*lst[1:])