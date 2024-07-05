import sys
input = sys.stdin.readline

x,y = map(int,input().split())
month = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

date = sum(month[:x-1]) + y

if date > 7:
    print(day[date%7-1])
else:
    print(day[date-1])