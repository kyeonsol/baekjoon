import sys
input = sys.stdin.readline

n = int(input())
notcute = 0
cute = 0

for i in range(n):
    a = int(input())
    if a == 1:
        cute += 1
    else:
        notcute += 1
    
if notcute < cute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")