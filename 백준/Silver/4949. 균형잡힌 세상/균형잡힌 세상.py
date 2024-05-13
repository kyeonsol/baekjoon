import sys
input = sys.stdin.readline



while 1:
    stack = []
    a = input().rstrip()
    if a == '.':
        break
    for i in a: #a에서 돌기
        if i == '(' or i == '[': #(이거나 [이면 스택에 추가
            stack.append(i)
        elif i == ')': #)일 때
            if len(stack) == 0: #스택이 비어있다면 break
                print('no') 
                break
            else: #스택이 비어있지 않을 때
                if stack[-1] == '(': #스택의 마지막이 (라면
                    stack.pop()
                elif stack[-1] == '[':
                    print('no')
                    break
        elif i == ']':
            if len(stack) == 0:
                print('no')
                break
            else:
                if stack[-1] == '[':
                    stack.pop()
                elif stack[-1] == '(':
                    print('no')
                    break
    else:
        if len(stack) == 0:
            print('yes')
        else:
            print('no')