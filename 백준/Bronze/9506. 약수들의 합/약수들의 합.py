while 1:
    n = int(input())
    if n == -1:
        break
    lst = []
    for i in range(1,n):
        if n % i == 0:
            lst.append(i)
    if sum(lst) == n:
        result = ""
        for i in lst:
            result += str(i) + " + "
        result = result[:-3]
        print(n, '=', result)
    else:
        print(n,"is NOT perfect.")