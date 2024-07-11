import sys
input = sys.stdin.readline

n = int(input())
num = n
cnt = 0

while 1:
    a = num//10 #십의자리
    b = num%10 #일의자리
    c = (a+b)%10 #더해서 일의자리
    num = (b*10)+c
    cnt += 1
    
    if n == num:
        break

print(cnt)