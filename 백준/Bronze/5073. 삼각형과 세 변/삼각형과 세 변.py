while 1:
    a,b,c = map(int,input().split())
    lst = [a,b,c]
    lst.sort()

    if a == 0 and b == 0 and c == 0:
        break
    
    if lst[2] >= lst[0] + lst[1]:
        print('Invalid')

    elif a == b == c:
        print('Equilateral')
    
    elif a == b or b == c or a == c:
        print('Isosceles')

    else:
        print('Scalene')