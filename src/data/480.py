n, q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n - 1)]
cd = [list(map(int, input().split())) for _ in range(q)]
r = [[] for _ in range(n)]
for i, j in ab:
    r[i - 1].append(j - 1)
    r[j - 1].append(i - 1)
a = [0] * n
b = [(0, 0)]
c = [False] * n
c[0] = True
while b:
    i, j = b.pop()
    j += 1
    for k in r[i]:
        if c[k]:
            continue
        a[k] = j
        b.append((k, j))
        c[k] = True
for i, j in cd:
    if a[i - 1] % 2 == a[j - 1] % 2:
        print("Town")
    else:
        print("Road")
