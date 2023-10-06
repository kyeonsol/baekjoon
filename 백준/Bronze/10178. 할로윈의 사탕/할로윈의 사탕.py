import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    candy, fam = map(int,input().split())
    a = candy // fam
    b = candy % fam
    print(f'You get {a} piece(s) and your dad gets {b} piece(s).')