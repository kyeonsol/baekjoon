import sys
input = sys.stdin.readline

n = int(input())
a = input().rstrip()
word = ''

for i in range(len(a)):
    if a[i] == '4' or a[i] == '5':
        if word[-2:] == 'PS':
            continue
        else:
            word += a[i]
    else:
        word += a[i]

print(word)