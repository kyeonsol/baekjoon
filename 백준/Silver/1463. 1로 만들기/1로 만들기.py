import sys
input = sys.stdin.readline

n = int(input())
d = [0]*(n+1) #0은 버리고 1부터 써야해서 n+1

for i in range(2,n+1): #1로 만들기 -> 1은 이미 1이라 0번 skip
    d[i] = d[i-1]
    if i%2 == 0: #2로 나누어 떨어지는지 = 유효한지
        d[i] = min(d[i],d[i//2])
    if i%3 == 0: #3으로 나누는 게 더 작으면 값이 바뀌어야 함 =! elif
        d[i] = min(d[i],d[i//3])
    d[i] += 1 #과정을 거쳤다면 횟수 더해주기

print(d[n])