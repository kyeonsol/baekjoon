import sys
input = sys.stdin.readline

lst = []

for i in range(7):
    a = int(input())
    if a % 2 != 0:
        lst.append(a)
    
if len(lst) == 0:
    print(-1)
else:
    lst = sorted(lst)
    print(sum(lst))
    print(lst[0])