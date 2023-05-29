a= input().upper()
a_set= list(set(a))

lst= []

for i in a_set:
    lst.append(a.count(i))

if lst.count(max(lst))>1:
    print("?")

else:
    print(a_set[lst.index(max(lst))])
