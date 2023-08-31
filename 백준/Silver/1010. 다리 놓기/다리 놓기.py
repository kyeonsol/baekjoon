import sys
input = sys.stdin.readline

def factorial(n): 
    answer = 1
    for i in range(1,n+1):
        answer *= i
    return answer

def bino_coef_factorial(n,m):  #이항계수
    return factorial(n) // factorial(m) // factorial(n-m)

t = int(input())

for i in range(t):
    n,m = map(int,input().split())
    print(bino_coef_factorial(m,n))