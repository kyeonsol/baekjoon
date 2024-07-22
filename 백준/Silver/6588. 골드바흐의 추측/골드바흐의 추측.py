import sys
input = sys.stdin.readline

#소수
s = [True] * 1000001

for i in range(2,int(1000001**0.5)):
    if s[i]:
        for j in range(i+i,1000001,i):
            s[j] = False

while 1:
    n = int(input())
    if n == 0:
        break

    for i in range(n-3,2,-2):  
        if s[i] and s[n-i] :
            print(f"{n} = {n-i} + {i}")
            break
    else:
        print('"Goldbach\'s conjecture is wrong."')

