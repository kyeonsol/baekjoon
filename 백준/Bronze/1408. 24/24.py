import sys
input = sys.stdin.readline

hour1, min1, sec1 = map(int,input().split(':'))
hour2, min2, sec2 = map(int,input().split(':'))

total = (hour2*3600 + min2*60 + sec2) - (hour1*3600 + min1*60 + sec1)

if total < 0:
    total += 3600*24

hour = total // 3600
min = (total%3600) // 60
sec = total % 60

print("%02d:%02d:%02d" %(hour,min,sec))