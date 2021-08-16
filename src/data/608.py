# N: 頂点数
# G[v]: 頂点vの子頂点 (親頂点は含まない)
#
# - construct
# prv[u] = v: 頂点uの一つ上の祖先頂点v
# - lca
# kprv[k][u] = v: 頂点uの2^k個上の祖先頂点v
# depth[u]: 頂点uの深さ (根頂点は0)
import sys

sys.setrecursionlimit(500000)
N, Q = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

# N: 頂点数
# G[v]: 頂点vの子頂点 (親頂点は含まない)

# Euler Tour の構築
S = []
F = [0] * 200000
depth = [-1] * 200000


def dfs(v, d):
    F[v] = len(S)
    depth[v] = d
    S.append(v)
    for w in G[v]:
        if depth[w] == -1:
            dfs(w, d + 1)
        S.append(v)


depth[0] = 0
dfs(0, 0)
for i in range(Q):
    c, d = map(int, input().split())
    if (depth[c - 1] + depth[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
