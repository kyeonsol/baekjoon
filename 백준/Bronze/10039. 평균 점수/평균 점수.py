import sys
input = sys.stdin.readline
lst = []

for i in range(5):
    a = int(input())
    if a < 40:
        lst.append(40)
    else:
        lst.append(a)

print(sum(lst)//5)