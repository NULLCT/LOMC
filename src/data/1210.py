import sys

ipt = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, Q = map(int, ipt().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, ipt().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

qq = [list(map(int, ipt().split())) for _ in range(Q)]

# Euler Tour Technique
S = []
FS = [0] * N
depth = [0] * N


def dfs(v, p, d):
    depth[v] = d
    FS[v] = len(S)
    S.append(v)
    for w in G[v]:
        if w == p:
            continue
        dfs(w, v, d + 1)
        S.append(v)


dfs(0, -1, 0)

# Sparse Table
L = len(S)
lg = [0] * (L + 1)
for i in range(2, L + 1):
    lg[i] = lg[i >> 1] + 1
st = [None] * (lg[L] + 1)
st0 = st[0] = S
b = 1
for i in range(lg[L]):
    st0 = st[i + 1] = [
        p if depth[p] <= depth[q] else q for p, q in zip(st0, st0[b:])
    ]
    b <<= 1


# LCA O(1)
def query(u, v):
    x = FS[u]
    y = FS[v]
    if x > y:
        x, y = y, x
    l = lg[y - x + 1]
    px = st[l][x]
    py = st[l][y - (1 << l) + 1]
    return px if depth[px] <= depth[py] else py


visited = [False] * N
Dist = [0] * N
Depth = [0] * N
Pare = [-1] * N


def rec(cur, dist):
    Dist[cur] = dist
    depth = 0
    visited[cur] = True
    for nxt in G[cur]:
        if visited[nxt]:
            continue
        Pare[nxt] = cur
        depth = max(depth, rec(nxt, dist + 1))
    Depth[cur] = depth
    return depth + 1


rec(0, 0)

for c, d in qq:
    c, d = c - 1, d - 1
    a = query(c, d)
    dis = Dist[c] + Dist[d] - 2 * Dist[a]
    if dis % 2:
        print("Road")
    else:
        print("Town")
