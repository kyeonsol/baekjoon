lst = ['A+','A0','B+','B0','C+','C0','D+','D0','F'] #등급
str = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0] #환산점수
total = 0 #학점총합
result = 0 #전공평점=점수*과목평점

for i in range(20):
    a,b,c = input().split() #b=학점 c=등급
    b = float(b)
    if c!='P':
        total += b
        result += (b*str[lst.index(c)])

print('%.6f' %(result / total))