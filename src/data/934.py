from collections import defaultdict
import sys

sys.setrecursionlimit(10**9)

N, Q = map(int, input().split())

_G = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    _G[a].append(b)
    _G[b].append(a)

depth = [-1] * N
depth[0] = 0

q = [0]
while q:
    pa = q.pop()
    for to in _G[pa]:
        if depth[to] != -1:
            continue
        depth[to] = depth[pa] + 1
        q.append(to)

G = defaultdict(list)
for i in range(N):
    for node in _G[i]:
        if depth[node] > depth[i]:
            G[i].append(node)

S = []
F = [0] * N
depth = [0] * N


def dfs(v, d):
    F[v] = len(S)
    depth[v] = d
    S.append(v)
    for w in G[v]:
        dfs(w, d + 1)
        S.append(v)


dfs(0, 0)

INF = (N, None)
M = 2 * N
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


for _ in range(Q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    lca = query(c, d)
    dist = depth[c] + depth[d] - 2 * depth[lca]
    if dist % 2 == 0:
        print("Town")
    else:
        print("Road")
