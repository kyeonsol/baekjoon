import sys
input = sys.stdin.readline

m = int(input())
lst = []

for i in range(m):
    a = input().strip()
    if a == 'all':
        lst = [i for i in range(1,21)]
    elif a == 'empty':
        lst.clear()
    else:
        a, b = a.split()
        b = int(b)
        if a == 'add':
            if b not in lst:
                lst.append(b)
        if a == 'remove':
            if b in lst:
                lst.remove(b)
        if a == 'check':
            if b in lst:
                print(1)
            else:
                print(0)
        if a == 'toggle':
            if b in lst:
                lst.remove(b)
            else:
                lst.append(b)
    
    