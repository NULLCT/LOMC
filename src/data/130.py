n, q = map(int, input().split())

p = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    p[a - 1].append(b - 1)
    p[b - 1].append(a - 1)

s = [0]
v = [False] * n
v[s[0]] = True
l = [0] * n
while s:
    ss = s.pop(0)
    for sss in p[ss]:
        if v[sss] == False:
            s.append(sss)
            v[sss] = True
            l[sss] = l[ss] + 1

for _ in range(q):
    c, d = map(int, input().split())
    ll = abs(l[c - 1] - l[d - 1])

    if ll % 2 == 0:
        print("Town")
    else:
        print("Road")
