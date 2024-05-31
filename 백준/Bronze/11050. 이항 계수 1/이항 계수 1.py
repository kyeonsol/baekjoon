import sys
input = sys.stdin.readline

def fac(x):
    total = 1
    for i in range(2,x+1):
        total *= i
    return total

n, k = map(int,input().split())
m, l = max(n,k), min(n,k) #m>l

print(int(fac(m)/(fac(l)*fac(m-l))))