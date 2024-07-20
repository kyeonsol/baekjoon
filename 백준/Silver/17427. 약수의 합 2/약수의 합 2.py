import sys
input = sys.stdin.readline

n = int(input())
t = 0
#f(n) = n의 약수의 합
#g(n) = n 이하의 f(n)의 합

for i in range(1,n+1):
    t += (n//i)*i

print(t)