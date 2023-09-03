import sys
input = sys.stdin.readline
from collections import Counter

n,m = map(int,input().split())
lst = []

for i in range(n):
    a = input().strip()
    if len(a) >= m:
        lst.append(a)

result = Counter(lst).most_common()
result.sort(key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in result:
    print(i[0])