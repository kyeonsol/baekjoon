import sys
input = sys.stdin.readline

n = int(input())
stack = []
score = []

for i in range(n):
    a = list(map(int,input().split()))
    if a == [0]:
        if len(stack) != 0:
            stack[-1][1] -= 1   
            if stack[-1][1] == 0:
                score.append(stack[-1][0])
                stack.pop()
    else:
        stack.append(a[1:])
        stack[-1][1] -= 1
        if stack[-1][1] == 0:
            score.append(stack[-1][0])
            stack.pop()

print(sum(score))
