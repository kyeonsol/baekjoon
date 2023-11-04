import sys
input = sys.stdin.readline

def bubble_sort(arr):
    cnt = 0
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                cnt += 1
    return cnt

p = int(input())

for i in range(p):
    lst = list(map(int,input().split()))
    count, people = lst[0], lst[1:]
    print(count, bubble_sort(people))
