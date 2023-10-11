import sys
input = sys.stdin.readline
passenger = 0
lst = []

for i in range(4):
    a, b = map(int,input().split())
    passenger += (b-a)
    lst.append(passenger)
    
print(max(lst))