import math
import sys
input = sys.stdin.readline

a, i = map(int,input().split())
cnt = ((i-1) * a) + 1

print(cnt)