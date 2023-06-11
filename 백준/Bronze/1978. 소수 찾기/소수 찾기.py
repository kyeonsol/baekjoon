n = int(input())
cnt = 0
a = list(map(int,input().split()))

for _ in a:
    error = 0
    if _ > 1:
        for i in range(2,_):
            if _ % i == 0:
                error += 1
        if error == 0:
            cnt += 1

print(cnt)