import sys

sys.setrecursionlimit(10**6)

n, q = [int(_) for _ in input().split()]
adj = [[] for i in range(n)]

lvl = [0] * n

for i in range(n - 1):
    a, b = [int(_) for _ in input().split()]
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

visited = [False] * n


def dfs(node):
    if visited[node]:
        return
    visited[node] = True
    for v in adj[node]:
        if not visited[v]:
            lvl[v] = lvl[node] + 1
            dfs(v)


dfs(0)

for i in range(q):
    u, v = [int(_) for _ in input().split()]
    print("Town" if (lvl[u - 1] - lvl[v - 1]) % 2 == 0 else "Road")
