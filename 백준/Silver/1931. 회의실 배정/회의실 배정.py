import sys
input = sys.stdin.readline

n = int(input())
lst = []
time = 0 #현재 회의의 끝나는 시간
cnt = 0 #회의 개수

for i in range(n):
    lst.append(list(map(int,input().split()))) #리스트에 회의 시간 저장

lst.sort(key = lambda x : (x[1],x[0])) #회의가 끝나는 시간을 기준으로 정렬

for i in range(n):
    if lst[i][0] < time:
        continue
    else:
        time = lst[i][1] #현재 회의가 끝나는 시간을 갱신
        cnt += 1

print(cnt)