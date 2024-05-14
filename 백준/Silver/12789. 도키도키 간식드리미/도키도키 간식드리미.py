import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
stack = []
cnt = 1

for i in range(n):
    if lst[0] == cnt: #번호와 같을 때
        lst.pop(0) #빼고 번호를 1 늘림
        cnt += 1
    else: #다를 때
        stack.append(lst[0])
        lst.pop(0)
    
    while len(stack) != 0:
        if stack[-1] == cnt:
            stack.pop(-1)
            cnt += 1
        else:
            break
       
if len(stack) != 0:
    print('Sad')
else:
    print('Nice')