import sys
input = sys.stdin.readline

n,m = map(int,input().split()) #세로, 가로
lst = []

for i in range(n):
    lst.append(input().strip()) #체스판 받기

res = 64

for i in range(0,n-7): #세로
    for j in range(0,m-7): #가로
        b_cnt = 0
        w_cnt = 0

        for x in range(i,i+8): #체스판 생성
            for y in range(j,j+8):

                if (x+y)%2 == 0 and lst[x][y] == 'W': #하얀색으로 시작 == 좌표를 더한 값이 짝수인 곳이 W여야 함
                    w_cnt += 1 #옳으면 추가
                elif (x+y)%2 != 0 and lst[x][y] == 'B': #검은색으로 시작 == 좌표를 더한 값이 홀수인 곳이 B여야 함
                    b_cnt += 1

        temp = 64- (w_cnt + b_cnt) #틀린 수
        res = min(res, temp, 64-temp) #전체 - w일 때 옳은 수 == b일 때 틀린 수

print(res)