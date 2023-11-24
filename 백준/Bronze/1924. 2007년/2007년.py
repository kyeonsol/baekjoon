import sys
input = sys.stdin.readline

a = [31,28,31,30,31,30,31,31,30,31,30,31]
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day = 0

x, y = map(int,input().split())

for i in range(0,x-1):
    day += a[i]

day = (day + y) % 7

print(week[day])