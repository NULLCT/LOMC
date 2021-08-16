n, q = map(int, input().split())

f = [-1 for i in range(n)]
v = [list() for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    v[a].append(b)
    v[b].append(a)

que = [(0, 1)]
f[0] = 1
while (que):
    e = que.pop()
    for vv in v[e[0]]:
        if not f[vv] == -1 or not v[vv]:
            continue
        else:
            f[vv] = e[1] ^ 1
            que.append((vv, e[1] ^ 1))

for i in range(q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if f[c] ^ f[d] == 1:
        print("Road")
    else:
        print("Town")
