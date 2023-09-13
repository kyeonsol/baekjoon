a, b = map(int,input().split())
k, x = map(int,input().split())

if a <= k-x and b >= k-x:
    if b < k+x:
        print(b-(k+x)+1)
    else:
        print((k+x)-(k-x)+1)

elif a <= k+x and b >= k+x:
    if a > k-x:
        print((k+x)-a+1)
    else:
        print((k+x)-(k-x)+1)

elif a > k-x and b < k+x:
    print(b-a+1)
else:
    print('IMPOSSIBLE')    