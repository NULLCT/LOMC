n, Q = map(int, input().split())
g = [[] for i in range(n)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)
d = [0] * n
q = [[-1, 0]]
while q:
    par, ver = q.pop()
    for to in g[ver]:
        if par == to:
            continue
        d[to] = d[ver] + 1
        q.append([ver, to])
for _ in range(Q):
    u, v = map(int, input().split())
    if (d[u - 1] + d[v - 1]) % 2:
        print("Road")
    else:
        print("Town")
