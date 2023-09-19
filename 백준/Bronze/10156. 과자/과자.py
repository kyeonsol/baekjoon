#과자 한 개의 가격 K 
#사려고 하는 과자의 개수 N
#현재 가진 돈의 액수 M
#print 모자란 돈

import sys
input = sys.stdin.readline

k, n, m = map(int,input().split())

if (k*n)-m >= 0:
    print((k*n)-m)
else:
    print(0)