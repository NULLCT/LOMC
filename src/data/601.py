def dfs(cur, prev):
    global depth, parent
    depth[cur] = depth[prev] + 1
    parent[cur][0] = prev
    for next_ in tree[cur]:
        if next_ != prev:
            dfs(next_, cur)


def addEdge(u, v):
    global tree
    tree[u].append(v)
    tree[v].append(u)


def precompute(n):
    for i in range(1, level):
        for node in range(1, n + 1):
            if parent[node][i - 1] != -1:
                parent[node][i] = parent[parent[node][i - 1]][i - 1]


def lca(u, v):
    if depth[v] < depth[u]:
        u, v = v, u

    diff = depth[v] - depth[u]

    for i in range(level):
        if ((diff >> i) & 1):
            v = parent[v][i]

    if u == v:
        return u

    for i in range(level - 1, -1, -1):
        if (parent[u][i] != parent[v][i]):
            u = parent[u][i]
            v = parent[v][i]

    return parent[u][0]


import sys

sys.setrecursionlimit(200002)

MAXN = 200002
level = 1

tree = [[] for _ in range(MAXN)]
depth = [0 for _ in range(MAXN)]
parent = [[-1 for _ in range(level)] for _ in range(MAXN)]

n, q = map(int, input().split())
for _ in range(n - 1):
    a, b = map(int, input().split())
    addEdge(a, b)

depth[0] = 0
dfs(1, 0)

for i in range(q):
    c, d = map(int, input().split())
    if (depth[c] + depth[d] - 2 * lca(c, d)) % 2 != 0:
        print("Road")
    else:
        print("Town")
