import sys
input = sys.stdin.readline

lst = list(map(int,input().split()))

twenty = lst.index(20)

if twenty == 0:
    alice = (lst[0]+lst[1]+lst[-1])/3
elif twenty == 19:
    alice = (lst[-2]+lst[-1]+lst[0])/3
else:
    alice = (lst[twenty-1]+lst[twenty]+lst[twenty+1])/3

bob = sum(lst)/20

if alice<bob:
    print('Bob')
elif alice>bob:
    print('Alice')
else:
    print('Tie')