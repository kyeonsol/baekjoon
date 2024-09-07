import sys
input = sys.stdin.readline

lst= ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
t, n = map(int,input().split())
total =  0

for i in range(n):
    d1, t1, d2, t2 = input().split()
    t -= 24*(lst.index(d2)-lst.index(d1))-int(t1)+int(t2)

if t<0:
    print(0)
elif t>48:
    print(-1)
else:
    print(t)