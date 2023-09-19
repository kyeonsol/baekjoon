import sys
input = sys.stdin.readline

#주사위 3개
#같은 눈 3개 = 10,000원+(같은 눈)×1,000
#같은 눈 2개 = 1,000원+(같은 눈)×100
#모두 다른 눈 =  (그 중 가장 큰 눈)×100

n = int(input())
lst = []

for i in range(n):
    a, b, c = map(int,input().split())
    if a == b == c:
        lst.append(10000+(1000*a))
    elif a == b:
        lst.append(1000+(100*a))
    elif c == b:
        lst.append(1000+(100*c))
    elif a == c:
        lst.append(1000+(100*a))
    else:
        lst.append(max(a,b,c)*100)

print(max(lst))

