n= int(input())
cnt=0

for i in range(n):
    a= input()
    if list(a)== sorted(a,key=a.find):
        cnt +=1

print(cnt)