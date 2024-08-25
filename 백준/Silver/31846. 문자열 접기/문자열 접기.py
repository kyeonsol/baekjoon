import sys
input = sys.stdin.readline

n = int(input())
s = list(input().rstrip())
q = int(input())

for i in range(q):
    l,r = map(int,input().split()) #시작, 끝
    l-=1
    r-=1
    total = 0

    for j in range(l,r+1): #한번씩 접어봄
        cnt = 0 #접었을 때 겹치는 횟수
        origin = s[l:j+1] 
        word = s[j+1:r+1][::-1] #접고 뒤집기

        for k in range(min(len(origin),len(word))): #짧은 종이 기준
            if origin[-k-1] == word[-k-1]: #뒤에서부터 비교하기
                cnt += 1
        if cnt > total:
            total = cnt 

    print(total)