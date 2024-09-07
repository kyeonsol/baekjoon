import sys
input = sys.stdin.readline

n = int(input()) #20~23 / 0~3
m = int(input()) #5~10

if n > 4:
    print(m+(24-n))

else:
    print(m-n)