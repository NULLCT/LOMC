import sys

sys.setrecursionlimit(500000)
n, q = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
c = [0] * q
d = [0] * q
for i in range(q):
    c[i], d[i] = map(int, input().split())
    c[i] -= 1
    d[i] -= 1
S = []
F = [0] * n
depth = [0] * n
seen = [0] * n


def dfs(v, e):
    F[v] = len(S)
    depth[v] = e
    S.append(v)
    seen[v] = 1
    for w in adj[v]:
        if not seen[w]:
            dfs(w, e + 1)
            S.append(v)


dfs(0, 0)

INF = (n, None)

M = 2 * n
M0 = 2**(M - 1).bit_length()
data = [INF] * (2 * M0)
for i, v in enumerate(S):
    data[M0 - 1 + i] = (depth[v], i)
for i in range(M0 - 2, -1, -1):
    data[i] = min(data[2 * i + 1], data[2 * i + 2])


def _query(a, b):
    yield INF
    a += M0
    b += M0
    while a < b:
        if b & 1:
            b -= 1
            yield data[b - 1]
        if a & 1:
            yield data[a - 1]
            a += 1
        a >>= 1
        b >>= 1


def query(u, v):
    fu = F[u]
    fv = F[v]
    if fu > fv:
        fu, fv = fv, fu
    return S[min(_query(fu, fv + 1))[1]]


for i in range(q):
    lca = query(c[i], d[i])
    ans = depth[c[i]] + depth[d[i]] - 2 * depth[lca]
    if ans % 2 == 0:
        print("Town")
    else:
        print("Road")
