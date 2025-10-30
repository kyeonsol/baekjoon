import sys
input = sys.stdin.readline

n = list(input().rstrip())
lst = [0 for i in range(10)]

for i in n:
    i = int(i) #9
    if i == 9 or i == 6:
        if lst[6]<lst[9]:
            lst[6]+=1
        else:
            lst[9]+=1
    else:
        lst[i] += 1

print(max(lst))