a,b,c= map(int,input().split())

if a==b==c:
    print(10000+(a*1000))

elif a==b or c==a:
    print(1000+(a*100))

elif b==c:
    print(1000+(b*100))

else:
    d=[a,b,c]
    d.sort()
    print(d[2]*100)
