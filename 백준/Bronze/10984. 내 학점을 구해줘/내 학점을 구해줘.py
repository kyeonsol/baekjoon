import sys
input = sys.stdin.readline

t = int(input())
h = 0
gpa = 0

for i in range(t):
    n = int(input())
    for j in range(n):
        c, g = input().split()
        c = int(c)
        g = float(g)
        h += c
        gpa += g*c
    gpa = round(gpa/h,1)
    print(h,gpa,sep=' ')
    h = 0
    gpa = 0
        