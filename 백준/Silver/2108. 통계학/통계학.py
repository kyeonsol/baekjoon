import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

lst.sort()

print(round(sum(lst)/n))
print(lst[n//2])

temp = Counter(lst).most_common()
if len(temp) > 1:
    if temp[0][1] == temp[1][1]:
        print(temp[1][0])
    else:
        print(temp[0][0])
else:
    print(temp[0][0])

print(max(lst) - min(lst))