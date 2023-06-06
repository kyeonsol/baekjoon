t = int(input())
lst = [25, 10, 5, 1]

for _ in range(t):
    c = int(input())
    q = []
    for i in lst:
        q.append(c // i)
        c = c % i
    print(*q)


