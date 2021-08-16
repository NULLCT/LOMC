import sys

sys.setrecursionlimit(10**9)


def dfs(G, v, p, d):
    depth[v] = d
    for nv in G[v]:
        if nv == p: continue
        dfs(G, nv, v, d + 1)


n, q = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

depth = [0] * n
dfs(G, 0, -1, 0)
for _ in range(q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if (depth[c] + depth[d]) % 2 == 0: print('Town')
    else: print('Road')
