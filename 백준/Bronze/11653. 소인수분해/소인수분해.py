import sys
input = sys.stdin.readline

n = int(input())
res = []

while 1:
    if n == 1:
        break
    else:
        for i in range(2,n+1):   
            if n%i == 0:  #1부터 n까지 돌며 나누기
                res.append(i)
                n = n//i  #n을 몫으로 바꾸기
                break  #반복

print(*res,sep='\n')