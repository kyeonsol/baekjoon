import sys
input = sys.stdin.readline

lst = list(map(int,input().split()))
cnt = []

for i in range(5):
    for j in range(1,5):
        for k in range(2,5):
            if i>=j or j>=k or k==i:
                continue
            else:
                tri = [lst[i],lst[j],lst[k]]
                m = max(tri)
                if m < sum(tri)-m : #작은 거 2개의 합 >= 가장 긴 것
                    sorted(tri)
                    if tri not in cnt:
                        cnt.append(tri)

print(len(cnt))