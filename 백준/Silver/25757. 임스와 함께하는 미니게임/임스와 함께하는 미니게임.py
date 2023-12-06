import sys
input = sys.stdin.readline

n, g = input().rstrip().split()
lst = [input() for i in range(int(n))]
lst = list(set(lst))

if g == 'Y':
        print(len(lst))
elif g == 'F':
        print(len(lst)//2)
else:
        print(len(lst)//3)
