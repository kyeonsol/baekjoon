import sys
input = sys.stdin.readline



while 1:
    n = int(input())
    lst = [] #n의 약수가 담긴 리스트
    if n == -1:
        break

    for i in range(1,n): #약수구하기
        if n%i == 0:  
            lst.append(i)
            
    if sum(lst) == n: #약수의 합이 n과 같으면
        print(f"{n} = ",end='')
        print(*lst,sep=' + ')
    else:
        print(f"{n} is NOT perfect.")