n = input()
lst = []

for i in str(n):
    lst.append(int(i))

lst.sort(reverse=True)

print(*lst,sep='')