n = int(input())
cnt = 0

for i in range(n):
    lst = []
    str = list(input())
    lst.append(str[0])
    flag = True
    for j in range(len(str)-1):
        if str[j] != str[j+1]:
            if str[j+1] not in lst:
                lst.append(str[j+1])
            else:
                flag = False
        else:
            continue
    if flag == True:
        cnt += 1

print(cnt)
        
        

            

#전글자와 다음 글자가 다른가?
#네 : 그렇다면 다음 글자가 이미 나온 글자인가?
#    네 : 탈락
#    아니오 : 리스트에 넣고 계속 진행
#아니오 : 계속 진행