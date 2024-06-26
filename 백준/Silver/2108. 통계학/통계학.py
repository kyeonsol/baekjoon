import sys
input = sys.stdin.readline

n = int(input())
lst = list()

for i in range(n):
    lst.append(int(input()))

lst.sort()

print(round(sum(lst)/n)) #산술평균
print(lst[len(lst)//2]) #중앙값

dic = {}
#최빈값, 범위
for i in lst:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 0

m = max(dic.values())
m_lst = []

for i in dic:
    if m == dic[i]:
        m_lst.append(i)

if len(m_lst) == 1:
    print(m_lst[0])
else:
    print(m_lst[1])

print(lst[-1]-lst[0])