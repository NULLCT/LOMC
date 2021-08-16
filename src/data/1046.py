from collections import deque

N, q = map(int, input().split())
ab = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    ab[a - 1].append(b - 1)
    ab[b - 1].append(a - 1)

cd = [list(map(int, input().split())) for _ in range(q)]

prev = [None] * N
dep = [1 << 60 for _ in range(N)]
dep[0] = 0
l = deque([0])
while len(l) > 0:
    u = l.popleft()
    for v in ab[u]:
        if dep[u] + 1 < dep[v]:
            dep[v] = dep[u] + 1
            l.append(v)
            prev[v] = u

# N: 頂点数
# G[v]: 頂点vの子頂点 (親頂点は含まない)
#
# - construct
# prv[u] = v: 頂点uの一つ上の祖先頂点v
# - lca
# kprv[k][u] = v: 頂点uの2^k個上の祖先頂点v
# depth[u]: 頂点uの深さ (根頂点は0)

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


kprev = construct(prev)
for c, d in cd:
    c -= 1
    d -= 1
    p = lca(c, d, kprev, dep)
    w = (dep[c] - dep[p]) + (dep[d] - dep[p])
    if w % 2 == 0:
        print("Town")
    else:
        print("Road")
