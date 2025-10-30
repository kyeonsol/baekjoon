import sys
input = sys.stdin.readline

x = int(input())
cnt = 0
lst = [64,32,16,8,4,2,1]

if x in lst:
    print(1)

else:
    while 1:
        if x == 0:
            break
        for i in lst:
            if i<=x:
                x-=i
                cnt+=1

    print(cnt)