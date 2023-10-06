import sys
input = sys.stdin.readline

n = int(input())  #테스트케이스 개수

for i in range(n):
    s = int(input())  #자동차의 가격
    n = int(input())  #옵션의 개수
    for j in range(n):
        q, p = map(int,input().split())
        price = q*p
        s += price
    print(s)
