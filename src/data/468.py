import sys

sys.setrecursionlimit(10**6)

n, q = map(int, input().split())

G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)

D = [-1] * n


def dfs(v, d=0):
    D[v] = d
    for u in G[v]:
        if D[u] == -1: dfs(u, d + 1)


dfs(0)

for _ in range(q):
    c, d = map(lambda x: int(x) - 1, input().split())
    print('Road' if (D[c] + D[d]) % 2 else 'Town')
