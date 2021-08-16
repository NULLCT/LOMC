from sys import stdin
import math

n, q, *indata = map(int, stdin.read().split())
g = [[] for i in range(n + 1)]
offset = 0
for i in range(n - 1):
    s, t = indata[offset + 2 * i], indata[offset + 2 * i + 1]
    g[s].append(t)
    g[t].append(s)

maxd = int(math.floor(math.log2(n + 1))) + 1
par = [[-1 for i in range(maxd)] for i in range(n + 1)]
depth = [0 for i in range(n + 1)]

check = [0 for i in range(n + 1)]

que = [(1, 0, -1)]
while que:
    now, d, p = que.pop()
    par[now][0] = p
    depth[now] = d
    check[now] = True
    for i in g[now]:
        if not check[i]:
            que.append((i, d + 1, now))

#dfs(1,0,-1)

for i in range(1, maxd):
    for j in range(1, n + 1):
        par[j][i] = par[par[j][i - 1]][i - 1]


def lca(u, v):
    difd = depth[u] - depth[v]
    if difd < 0:
        u, v = v, u
        difd = -difd
    bitnum = 0
    while difd > 0:
        if difd & 1:
            u = par[u][bitnum]
        bitnum += 1
        difd = difd >> 1
    if u == v:
        return u
    else:
        for i in range(maxd):
            if par[u][maxd - i - 1] != par[v][maxd - i - 1]:
                u = par[u][maxd - i - 1]
                v = par[v][maxd - i - 1]
        return par[u][0]


offset += (n - 1) * 2
for i in range(q):
    s, t = indata[offset + 2 * i], indata[offset + 2 * i + 1]
    kari = depth[lca(s, t)]
    ans = depth[s] + depth[t] - kari * 2
    if ans % 2 == 0:
        print("Town")
    else:
        print("Road")
