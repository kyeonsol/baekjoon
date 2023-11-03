#거리두기 수칙
#세로줄번호 차 > n or 가로줄번호 차 > m
#전체 = w개씩 h행
import sys
input = sys.stdin.readline
import math

h, w, n, m = map(int,input().split())

a = math.ceil(h / (n+1))
b = math.ceil(w / (m+1))

print(a*b)