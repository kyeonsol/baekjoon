n = int(input())
lst = []

for i in range(n):
    name, dd, mm, yy = input().strip().split()
    dd, mm, yy = int(dd), int(mm), int(yy)
    lst.append((yy, mm, dd, name))

lst.sort()
print(lst[-1][3])
print(lst[0][3])

