import sys
input = sys.stdin.readline
import math

a,b = map(int,input().split())
c,d = map(int,input().split())

bunmo = b*d
bunja = a*d + b*c

i = math.gcd(bunmo,bunja)
A = bunja//i
B = bunmo//i

print(A,B,sep=' ')