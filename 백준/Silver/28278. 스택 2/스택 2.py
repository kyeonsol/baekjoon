import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    cmd = input().split()

    if cmd[0] == '1':
        stack.append(cmd[1])

    elif cmd[0] == '2':
        if len(stack) != 0:
            print(stack[-1])
            del(stack[-1])
        else:
            print(-1)

    elif cmd[0] == '3':
        print(len(stack))

    elif cmd[0] == '4':
        if len(stack) != 0:
            print(0)
        else:
            print(1)
            
    elif cmd[0] == '5':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)