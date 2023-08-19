import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    command = input().split()
    
    if command[0] == 'push':
        stack.append(command[1])
    
    elif command[0] == 'pop':
        if len(stack) != 0:
            print(stack[-1])
            del stack[-1]
        else:
            print(-1) 

    elif command[0] == 'size':
        if len(stack) != 0:
            print(len(stack))
        else:
            print(0)

    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)