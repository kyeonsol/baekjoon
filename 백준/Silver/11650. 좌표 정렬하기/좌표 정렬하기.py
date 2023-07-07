n = int(input())
lst = []

for i in range(n):
    [x,y] = map(int,input().split())
    lst.append([x,y])

s_lst = sorted(lst)

for i in range(n):
    print(s_lst[i][0],s_lst[i][1])