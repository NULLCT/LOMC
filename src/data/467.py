import sys

sys.setrecursionlimit(10**6)

n, q = map(int, input().split())

G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)

color = [-1] * n


def dfs(v, c=0):
    color[v] = c
    for u in G[v]:
        if color[u] == -1: dfs(u, 1 - c)


dfs(0)

for _ in range(q):
    c, d = map(lambda x: int(x) - 1, input().split())
    print('Road' if color[c] != color[d] else 'Town')
