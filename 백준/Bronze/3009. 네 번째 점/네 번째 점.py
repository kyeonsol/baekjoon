xlst = []
ylst = []

for i in range(3):
    x,y = map(int,input().split())
    xlst.append(x)
    ylst.append(y)

for i in range(3):
    if xlst.count(xlst[i]) == 1:
        x4 = xlst[i]
    if ylst.count(ylst[i]) == 1:
        y4 = ylst[i]

print(x4,y4)

