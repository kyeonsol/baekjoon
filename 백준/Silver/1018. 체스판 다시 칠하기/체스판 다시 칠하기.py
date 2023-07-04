n,m = map(int,input().split())
lst = []
error = []

for i in range(n):
    a = input()
    lst.append(a)

for i in range(n-7):
    for j in range(m-7):
        white = 0
        black = 0
        
        for k in range(i,i+8):  #열
            for l in range(j,j+8):  #행
                if (k+l)%2 == 0:  #짝수
                    if lst[k][l] != 'W':
                        white += 1
                    else:
                        black += 1
                else:
                    if lst[k][l] != 'B':
                        white += 1
                    else:
                        black += 1
        error.append(white)
        error.append(black)

print(min(error))