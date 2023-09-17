t = int(input())

for i in range(t):
    lst = list(map(str,input().split()))
    num = lst[0]
    for j in range(len(lst)):
        if j == 0:
            num = float(lst[j])
        elif lst[j] == '@':
            num *= 3
        elif lst [j] == '%':
            num += 5
        else:
            num -= 7
    print("{:.2f}".format(num))