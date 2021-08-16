import sys

sys.setrecursionlimit(4100000)
N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
color = [-1] * N


def dfs(x, par, now):
    color[x] = now
    for u in G[x]:
        if u != par and color[u] == -1:
            dfs(u, x, 1 - now)


dfs(0, -1, 0)
for _ in range(Q):
    c, d = map(int, input().split())
    if color[c - 1] == color[d - 1]:
        print('Town')
    else:
        print('Road')
