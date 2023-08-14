import sys
input = sys.stdin.readline

n = int(input())

def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

for i in range(n):
    a = int(input())
    while 1:
        if a == 0 or a == 1:
            print(2)
            break
        elif is_prime(a):
            print(a)
            break
        else:
            a += 1
