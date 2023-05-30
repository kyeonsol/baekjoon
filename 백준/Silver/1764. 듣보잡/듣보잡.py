import sys
input= sys.stdin.readline

n,m= map(int,input().split())
st=[]
st2=set()
ans=[]

for i in range(n):
    st.append(input().rstrip())
for i in range(m):   
    st2.add(input().rstrip())

for i in range(n):
    if st[i] in st2:
        ans.append(st[i])

ans.sort() 

print(len(ans))
print(*ans,sep='\n')