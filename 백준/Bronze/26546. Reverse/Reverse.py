import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    word = ''
    a,b,c = input().split()
    b,c = int(b),int(c)
    word += a[:b]
    word += a[c:]    
    print(word)