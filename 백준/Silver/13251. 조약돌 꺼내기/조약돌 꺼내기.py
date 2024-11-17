import sys
input = sys.stdin.readline

#같은 색일 확률 => 조합론
#분자 : n[0]Ck * n[1]Ck * ...
#분모 : 전체공의수Ck

def fac(x):
    a = 1
    for i in range(2,x+1):
        a *= i
    return a

def bino_fac(x,y):
    return fac(x)//fac(y)//fac(x-y)

m = int(input()) #색상
n = list(map(int,input().split())) #각 색상의 조약돌 개수
k = int(input()) #뽑는 개수


if m==1 or k==1: #색상이 하나거나 하나만 뽑으면 무조건 가능
    print(1.0)

sumnum = 0
for i in n:
    sumnum += bino_fac(i,k)
denominator = bino_fac(sum(n),k)

print(sumnum/denominator)