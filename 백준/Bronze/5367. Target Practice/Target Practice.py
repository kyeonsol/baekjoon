import sys
input = sys.stdin.readline

n = int(input())
lst = []

print('|'+'-'*(n-2)+'|')

for i in range(1,n//2):
    lst.append('|'+ ' '*(i-1) + '*' + ' '*((n-2)-2*i) + '*' + ' '*(i-1) +'|')
    print('|'+ ' '*(i-1) + '*' + ' '*((n-2)-2*i) + '*' + ' '*(i-1) +'|')

print('|'+' '*(n//2-1) + '*' + ' '*(n//2-1) + '|')

for i in range(1,n//2):
    print(lst[-i])

print('|'+'-'*(n-2)+'|')