import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
lst = list(range(1,n+1))
queue = deque(lst) #카드 생성
'''lst = deque([i for i in range(1,n+1)]) #deque 안에 많은 정보 넣지 말기!''' 

while 1:
    if len(queue) == 1:
        print(queue[0])
        break
    else:
        queue.popleft()
        if len(queue) == 1:
            print(queue[0])
            break
        else:
            queue.append(queue[0])
            queue.popleft()