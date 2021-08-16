from collections import defaultdict
from math import ceil, log2

n, q = map(int, input().strip().split())
tree = defaultdict(list)
for i in range(n - 1):
    u, v = map(int, input().strip().split())
    tree[u].append(v)
    tree[v].append(u)

level = dict()
visited = defaultdict(bool)

LEVEL = ceil(log2(n)) + 1
sparse = [[-1 for __ in range(LEVEL)] for ___ in range(n + 1)]


def dfs(u):
    st = [(u, 0)]
    while len(st):
        u, k = st.pop()
        visited[u] = True
        level[u] = k
        for v in tree[u]:
            if not visited[v]:
                st.append((v, k + 1))
                sparse[v][0] = u


dfs(1)

for i in range(1, LEVEL):
    for node in range(1, n + 1):
        if sparse[node][i - 1] != -1:
            sparse[node][i] = sparse[sparse[node][i - 1]][i - 1]


def lca(u, v):
    if level[v] < level[u]:
        u, v = v, u
    diff = level[v] - level[u]
    for i in range(LEVEL):
        if (diff >> i) & 1:
            v = sparse[v][i]
    if u == v:
        return u
    for i in reversed(range(LEVEL)):
        if sparse[u][i] != sparse[v][i] and sparse[u][i] != -1:
            u = sparse[u][i]
            v = sparse[v][i]
    return sparse[u][0]


for __ in range(q):
    u, v = map(int, input().strip().split())
    x = lca(u, v)
    dist = abs(level[x] - level[u]) + abs(level[x] - level[v])
    if dist & 1:
        print("Road")
    else:
        print("Town")
