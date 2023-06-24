n = int(input())
xlst = []
ylst = []

for i in range(n):
    a,b = map(int,input().split())
    xlst.append(a)
    ylst.append(b)

a = max(xlst) - min(xlst)
b = max(ylst) - min(ylst)

print(a*b)