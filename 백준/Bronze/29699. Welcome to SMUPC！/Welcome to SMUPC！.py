import sys
input = sys.stdin.readline

n = int(input())
str = "WelcomeToSMUPC"
lst = list(str)

if n < 15:
    print(lst[n-1])
else:
    while n > 14:
        n = n % 14
    print(lst[n-1])