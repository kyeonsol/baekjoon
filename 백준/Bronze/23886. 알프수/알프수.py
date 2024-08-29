import sys
input = sys.stdin.readline

x_inp = list(input().rstrip())
x = list(map(int,x_inp))
cha = []
flag = True

#알프수 = 오를 때, 내릴 때 등차수열이어야 한다.

for i in range(len(x)-1):
    num = x[i] - x[i+1]

    if num == 0: #flat
        flag = False
        break

    elif num < 0: #up hill
        if len(cha) == 0 or cha[-1] > 0:
            cha.append(num) # <0
        else:
            if num == cha[-1]:
                continue
            else:
                flag = False

    else: #down hill
        if len(cha) == 0 or cha[-1] < 0:
            cha.append(num) # >0
        else:
            if num == cha[-1]:
                continue
            else:
                flag = False

if len(cha) > 0 and (cha[0] > 0 or cha[-1] < 0): #처음이 오르막, 마지막이 내리막
    flag = False

if flag == True:
    print('ALPSOO')
else:
    print('NON ALPSOO')
        