import sys
input = sys.stdin.readline

m,n = map(int,input().split())

def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

for i in range(m,n+1):
    if i == 1:
        continue
    elif is_prime(i):
        print(i)