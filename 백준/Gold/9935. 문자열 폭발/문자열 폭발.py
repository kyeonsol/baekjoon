import sys
input = sys.stdin.readline

string = input().strip()
bomb = input().strip()

bomb_last = bomb[-1]
stack = []
len = len(bomb)

for i in string:
    stack.append(i)
    if i == bomb_last and ''.join(stack[-len:]) == bomb:
        del stack[-len:]

answer = ''.join(stack)

if answer == '':
    print('FRULA')
else:
    print(answer)