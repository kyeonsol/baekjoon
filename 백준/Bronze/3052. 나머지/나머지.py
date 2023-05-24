a=[]

for i in range(10):
    b=int(input())
    b=b%42
    a.append(b)

print(len(set(a)))