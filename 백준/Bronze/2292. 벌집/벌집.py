n = int(input())
floor = 1
six = 6
room = 1

while n > floor:
    room += 1
    floor += six
    six += 6

print(room)