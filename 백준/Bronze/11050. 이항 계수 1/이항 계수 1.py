import sys
input = sys.stdin.readline

def factorial(n):
    answer = 1
    for i in range(1,n+1):
        answer *= i
    return answer

n,k = map(int,input().split())

print(factorial(n)//factorial(k)//factorial(n-k))