c= int(input())

for i in range(c):
    lst= list(map(int,input().split()))
    avg= sum(lst[1:])/lst[0]
    cnt= 0
    for i in lst[1:]:
        if i>avg:
            cnt+= 1
    rate= cnt/lst[0]*100
    print(f'{rate:.3f}%')