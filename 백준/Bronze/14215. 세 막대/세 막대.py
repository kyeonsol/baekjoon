a,b,c = map(int,input().split())
lst = [a,b,c]
slst = sorted(lst)

if slst[0]==slst[1]==slst[2]:
    print(slst[0]*3)

elif slst[2] >= slst[0]+slst[1]:
    slst[2] = slst[0]+slst[1]-1
    print(slst[0]+slst[1]+slst[2])

else:
    print(a+b+c)

