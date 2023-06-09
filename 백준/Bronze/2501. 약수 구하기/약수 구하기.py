n,k = map(int,input().split())
i = 0
lst = []

for _ in range(n):
    i += 1
    m = n % i
    if m == 0:
        lst.append(i)
    else:
        continue

if len(lst) < k:
    print("0")
else:
    print(lst[k-1])