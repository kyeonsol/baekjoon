a,b= map(int,input().split())
c=int(input())

x=c//60
y=c%60

a=a+x
b=b+y

if b>=60:
    a=a+1
    b=b-60

if a>=24:
    a=a-24

print(a,b)