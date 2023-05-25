n=int(input())
lst=list(map(int,input().split()))
x=max(lst)

for i in range(n):
    lst[i]=lst[i]/x*100

print(sum(lst)/n)