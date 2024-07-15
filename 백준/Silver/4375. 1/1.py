import sys
input = sys.stdin.readline

one = '1'

while 1:
    try:
        n = int(input())
        num = 1
        while 1:
            if int(one*num) % n == 0:
                print(num)
                break
            else:
                num += 1
    except:
        break