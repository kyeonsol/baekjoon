import sys
input = sys.stdin.readline

t = int(input()) #testcase

for i in range(t):
    k = int(input()) #층
    n = int(input()) #호
    resident = [[(i+1) for i in range(n)]] #0층 n호까지 초기값 세팅
    
    for j in range(k): 
        a = 0
        a_zip = []
        for _ in range(n):
            a += resident[-1][_]
            a_zip.append(a)
        resident.append(a_zip)
    print(resident[k][n-1])
