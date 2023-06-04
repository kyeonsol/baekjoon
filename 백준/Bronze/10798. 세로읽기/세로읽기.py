lst = []

for i in range(5):
    lst.append(input())

sum = ''

for i in range(max(len(e) for e in lst)):
    for j in range(5):
        if i < len(lst[j]):
            print(lst[j][i], end='')