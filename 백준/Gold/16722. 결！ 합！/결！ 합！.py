import sys
input = sys.stdin.readline
score = 0
lst = []
ans = []
g_cnt = 0

for i in range(9):
    lst.append(list(input().split()))

#속성이 모두 같거나 달라야 함
for i in range(9):
    for j in range(i+1,9):
        for k in range(j+1,9):
            if (lst[i][0]==lst[j][0] and lst[j][0]==lst[k][0] and lst[i][0]==lst[k][0]) or (lst[i][0]!=lst[j][0] and lst[i][0]!=lst[k][0] and lst[j][0]!=lst[k][0]):
                if (lst[i][1]==lst[j][1] and lst[j][1]==lst[k][1] and lst[i][1]==lst[k][1]) or (lst[i][1]!=lst[j][1] and lst[i][1]!=lst[k][1] and lst[j][1]!=lst[k][1]):
                    if (lst[i][2]==lst[j][2] and lst[j][2]==lst[k][2] and lst[i][2]==lst[k][2]) or (lst[i][2]!=lst[j][2] and lst[i][2]!=lst[k][2] and lst[j][2]!=lst[k][2]):
                        ans.append([i+1,j+1,k+1])

n = int(input())
for i in range(n):
    a = input().split()
    if a[0] == 'H': #합을 외쳤을 때
        num = [int(a[1]),int(a[2]),int(a[3])]
        if sorted(num) in ans:
            score += 1
            ans.remove(sorted(num))
        else:
            score -= 1
    else: #결을 외쳤을 때
        if len(ans)==0:
            if g_cnt == 0:
                score += 3
                g_cnt += 1
            else:
                score -= 1
        else:
            score -= 1
            
print(score)
