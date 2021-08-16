n, q = map(int, input().split())
import sys

sys.setrecursionlimit(10**9)

E = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)

visited = set()
ranks = [0] * n


def dfs(G, node, rank):
    ranks[node] = rank
    visited.add(node)
    for child in G[node]:
        if child in visited:
            continue
        dfs(G, child, rank + 1)


dfs(E, 0, 0)

for i in range(q):
    c, d = map(lambda x: int(x) - 1, input().split())
    if (ranks[c] - ranks[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
