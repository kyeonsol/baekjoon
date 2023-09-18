import sys
input = sys.stdin.readline

a = int(input())
op = input().strip()
b = int(input())

if op == '+':
    print(a+b)
elif op == '*':
    print(a*b)