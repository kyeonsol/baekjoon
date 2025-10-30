import sys
input = sys.stdin.readline

#각 자리수를 내림차순으로 정렬
n = list(input().strip())

for i in n:
    i = int(i)

new_n = sorted(n,reverse=True)

for i in new_n:
    print(i,end='')