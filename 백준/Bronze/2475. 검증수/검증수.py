import sys
input = sys.stdin.readline

# 6번째 자리 고유번호의 처음 5자리에 
# 들어가는 5개의 숫자를 각각 제곱한 수의 
# 합을 10으로 나눈 나머지

list = list(map(int,input().split()))

for i in range(5):
    list[i] = list[i]**2

print(sum(list) % 10)