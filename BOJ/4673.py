n = set(range(1, 10001))
dn = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    dn.add(i)

selfnum = sorted(n - dn)
for i in selfnum:
    print(i)
