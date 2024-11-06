import sys
input = sys.stdin.readline

def fac(x):
    t = 1
    for i in range(1,x+1):
        t *= i
    return t

def bino_coef_fac(x,y):
    return fac(x)//fac(y)//fac(x-y)

n,k = map(int,input().split())

print(bino_coef_fac(n,k)%10007)