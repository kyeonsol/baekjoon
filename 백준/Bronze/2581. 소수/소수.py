m = int(input())
n = int(input())
lst = []

for i in range(m,n+1):
    error = 0
    if i > 1:
        for _ in range(2,i):
            if i % _ == 0:
                error += 1
                break
        if error == 0:
            lst.append(i)

if len(lst) > 0:
    print(sum(lst))
    print(lst[0])
    
else:
    print(-1)