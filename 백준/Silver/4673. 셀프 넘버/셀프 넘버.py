num = set(range(1,10000))
generated_num = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    generated_num.add(i)

selfnum = sorted(num-generated_num)
for i in selfnum:
    print(i)