a = input()
cnt = 10

for i in range(1,len(a)):
    if a[i] == a[i-1]:
        cnt += 5
    else:
        cnt += 10
print(cnt)