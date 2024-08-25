import sys
input = sys.stdin.readline

n,m = map(int,input().split())
song = []

for i in range(n):
    s = input().split()
    song.append(s[1:5])

for i in range(m):
    lst = input().split()
    same = []
    for j in range(n):
        if lst == song[j][1:]:
            same.append(song[j][0])
    if len(same) == 0:
        print('!')
    elif len(same) == 1:
        print(same[0])
    else:
        print('?')