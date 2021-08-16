n, q = map(int, input().split())

g = [[] for i in range(n)]
for i in range(n - 1):
    ai, bi = map(int, input().split())
    ai -= 1
    bi -= 1
    g[ai].append(bi)
    g[bi].append(ai)

# N: 頂点数
# G[v]: 頂点vの子頂点 (親頂点は含まない)
#
# - construct
# prv[u] = v: 頂点uの一つ上の祖先頂点v
# - lca
# kprv[k][u] = v: 頂点uの2^k個上の祖先頂点v
# depth[u]: 頂点uの深さ (根頂点は0)

N = n
LV = (N - 1).bit_length()


def construct(prv):
    kprv = [prv]
    S = prv
    for k in range(LV):
        T = [0] * N
        for i in range(N):
            if S[i] is None:
                continue
            T[i] = S[S[i]]
        kprv.append(T)
        S = T
    return kprv


def lca(u, v, kprv, depth):
    dd = depth[v] - depth[u]
    if dd < 0:
        u, v = v, u
        dd = -dd

    # assert depth[u] <= depth[v]
    for k in range(LV + 1):
        if dd & 1:
            v = kprv[k][v]
        dd >>= 1

    # assert depth[u] == depth[v]
    if u == v:
        return u

    for k in range(LV - 1, -1, -1):
        pu = kprv[k][u]
        pv = kprv[k][v]
        if pu != pv:
            u = pu
            v = pv

    # assert kprv[0][u] == kprv[0][v]
    return kprv[0][u]


# BFS
infty = 10**10
depth = [infty for i in range(n)]
prev = [infty for i in range(n)]

prev[0] = 0
depth[0] = 0
from collections import deque

dq = deque()
dq.append(0)

while len(dq):
    u = dq.popleft()
    for v in g[u]:
        if depth[v] == infty:
            depth[v] = depth[u] + 1
            prev[v] = u
            dq.append(v)

kprv = construct(prev)

for i in range(q):
    ci, di = map(int, input().split())
    ci -= 1
    di -= 1
    lc = lca(ci, di, kprv, depth)
    dist = depth[ci] + depth[di] - depth[lc] * 2
    if dist % 2 == 0:
        print("Town")
    else:
        print("Road")
