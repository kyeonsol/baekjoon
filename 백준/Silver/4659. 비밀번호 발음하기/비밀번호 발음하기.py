import sys
input = sys.stdin.readline

p = ['a','e','i','o','u']
m = ['ee','oo']

while 1:
    a = input().strip()
    if a == 'end': break
    
    else:
        flag1 = False
        for i in range(len(a)):
            if a[i] in p:
                flag1 = True

        flag2 = True
        for i in range(len(a)-2):
            tmp = a[i:i+3]
            if tmp[0] in p and tmp[1] in p and tmp[2] in p:
                flag2 = False
            elif tmp[0] not in p and tmp[1] not in p and tmp[2] not in p:
                flag2 = False
        
        flag3 = True
        for i in range(len(a)-1):
            tmp = a[i:i+2]
            if tmp not in m and tmp[0] == tmp[1]:
                flag3 = False
        
        if flag1 and flag2 and flag3:
            print(f"<{a}> is acceptable.")
        else:
            print(f"<{a}> is not acceptable.")
