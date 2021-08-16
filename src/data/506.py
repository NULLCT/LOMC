N, Q = map(int, input().split())
neighbors = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    neighbors[a - 1].append(b - 1)
    neighbors[b - 1].append(a - 1)
queries = []
for _ in range(Q):
    c, d = map(int, input().split())
    queries.append((c - 1, d - 1))

from collections import deque

# root: #0
# find depths
depths = [-1] * N
parents = [[-1] * N]  # [k of 2^k][i]
q = deque()
q.append((0, 0, -1))
while len(q):
    i, d, parent = q.popleft()  # BFS
    depths[i] = d
    parents[0][i] = parent
    for j in neighbors[i]:
        if parent == j:
            continue
        q.append((j, d + 1, i))
u = i  # one of the deepest
maxdepth = d

# doubling
logmaxdepth = 1
while (1 << logmaxdepth) <= maxdepth:
    logmaxdepth += 1
for k in range(logmaxdepth - 1):
    parents.append([-1] * N)
    for i in range(N):
        parents[k + 1][i] = parents[k][parents[k][i]]


def find_lca(u, v):
    if depths[u] < depths[v]:
        u, v = v, u  # ensure depths[u] >= depths[v]
    for k in range(logmaxdepth):
        if 1 & (depths[u] - depths[v]) >> k:
            u = parents[k][u]
    if u == v:
        return u
    for k in range(logmaxdepth - 1, -1, -1):
        if parents[k][u] != parents[k][v]:
            u = parents[k][u]
            v = parents[k][v]
    return parents[0][u]


def find_dist(u, v):
    return depths[u] + depths[v] - 2 * depths[find_lca(u, v)]


for c, d in queries:
    print("Road" if find_dist(c, d) % 2 else "Town")
