import sys
input = sys.stdin.readline

n = int(input())
lst = {}

for i in range(n):
    a,b = input().split()
    if b == 'enter':
        lst[a] = True
    else:
        del lst[a]

s_lst = sorted(lst,reverse=True)

print(*s_lst,sep='\n')