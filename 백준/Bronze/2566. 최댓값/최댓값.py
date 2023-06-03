lst = []
m = -1
x = 0
y = 0

for i in range(9):
    a = list(map(int,input().split()))
    lst.append(a)

for i in range(9):        #x==행
    for j in range(9):    #y==열
        if lst[i][j] > m:
            m = lst[i][j]
            x = i + 1
            y = j + 1
 
print(m)
print(x,y)