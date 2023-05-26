t=int(input())

for i in range(t):
    s,r=input().split()
    s= int(s)
    for i in r:
        print(i*s,end="")
    print()


