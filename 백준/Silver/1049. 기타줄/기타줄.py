import sys
input = sys.stdin.readline

n,m = map(int,input().split())
set_ = 1000
ind = 1000

for i in range(m):
    a,b = map(int,input().split())
    
    if set_ > a: #세트의 최솟값
        set_ = a
    if ind > b: #낱개의 최솟값
        ind = b


if n < 6:
    buy_1 = n*ind
    buy_2 = set_
    print(min(buy_1,buy_2))
elif n >= 6:
    n_ = n//6 #끊어진 기타줄을 세트로 나타내기
    mod = n%6
    buy1 = n_*set_ + mod*ind
    buy2 = n*ind
    buy3 = (n_+1)*set_
    print(min(buy1,buy2,buy3))
