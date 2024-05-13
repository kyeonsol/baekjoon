import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    stack = []
    a = input().strip()
    for j in a:
        if j == '(': #(가 나오면 스택에 저장
            stack.append(j)
        else: #)가 나온 후
            if len(stack) != 0: #)이 나오면 스택에서 하나 제거
                stack.pop()
            else: #스택이 비어있으면 NO
                print('NO')
                break
    else: #break가 안됨
        if len(stack) != 0:
            print('NO')
        else:
            print('YES')