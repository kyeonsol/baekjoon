import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split()) #총감독관, 부감독관 당 학생
res = 0

for i in range(len(a)):
    a[i] -= b
    res += 1
    if a[i] <= 0:
        continue
    elif a[i]%c == 0:
        res += a[i]//c
    else:
        res += (a[i]//c)+1

print(res)