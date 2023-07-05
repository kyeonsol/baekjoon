lst = []

for i in range(5):
    a = int(input())
    lst.append(a)

avg = sum(lst) // 5

lst.sort()
zhg = lst[2]

print(avg, zhg, sep='\n')