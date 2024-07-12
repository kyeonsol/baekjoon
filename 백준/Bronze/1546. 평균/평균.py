import sys
input = sys.stdin.readline

n = int(input()) #int
lst = list(map(int,input().split())) #list int
new = [] #list
m = max(lst) #int

for i in range(n): #int
    new.append(lst[i]/m*100)

print(sum(new)/n)