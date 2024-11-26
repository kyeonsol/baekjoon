import sys
input = sys.stdin.readline
#1~n의 순열 : n! -> 사전식 배열 정렬 가능

def fac(n):
    res = 1
    for i in range(2,n+1):
        res *= i
    return res

n = int(input())
lst = list(map(int,input().split()))

if lst[0] == 1: #순열 표현해내기
    k = lst[1]
    ans = []
    num = [i for i in range(1,n+1)]

    for i in range(1,n+1):
        #인덱스의 특성 고려해 k 대신 k-1
        #해당 숫자가 앞일 때, 생길 수 있는 수열의 개수 (n-i)!
        index = ((k-1)//fac(n-i)) 
        ans.append(num[index])
        #해당 수는 num에서 제거하여 반복해야 함
        #k도 갱신
        num.pop(index)
        k %= fac(n-i)
        if k == 1:
            for j in num:
                ans.append(j)
            break
        
    print(*ans)
            
elif lst[0] == 2: #해당 순열의 순서 찾기
    perm = lst[1:]
    num = [i for i in range(1,n+1)]
    res = 0
    for i in range(n):
        x = perm[i]
        index = num.index(x)
        res += (index*fac(n-i-1))
        num.pop(index)

    print(res+1)