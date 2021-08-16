import sys

sys.setrecursionlimit(2**31 - 1)
N, Q = list(map(int, input().split()))
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a] += [b]
    G[b] += [a]

prev = [None] * N
depth = [0] * N
seen = set()


def dfs(v, d):
    seen.add(v)
    depth[v] = d
    for i in G[v]:
        if i in seen: continue
        prev[i] = v
        dfs(i, d + 1)


prev[0] = 0
dfs(0, 0)

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


dp = construct(prev)
for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    lcaid = lca(c, d, dp, depth)
    dist = depth[c] + depth[d] - depth[lcaid] * 2
    if dist % 2 == 1:
        print("Road")
    else:
        print("Town")
