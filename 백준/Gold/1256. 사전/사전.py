import sys
input = sys.stdin.readline

def fac(x):
    res = 1
    for i in range(2,x+1):
        res *= i
    return res

n,m,k = map(int,input().split())
ans = []

#n개의 a와 m개의 z
#k번째 문자열이 무엇인지

#문자열의 개수로 -1출력 if문
if fac(n+m)//fac(n)//fac(m) < k:
    print(-1)
    exit(0)

#순열 만들기
while n>0 and m>0:
    if n>0:
        Afront = fac(n-1+m)//fac(n-1)//fac(m)
    else:
        Afront = 0

    if k <= Afront:
        ans.append('a')
        n -= 1
    else:
        ans.append('z')
        m -= 1
        k -= Afront

if n != 0:
    for i in range(n):
        ans.append('a')

if m != 0:
    for i in range(m):
        ans.append('z')

print(*ans,sep='')