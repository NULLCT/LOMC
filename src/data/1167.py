def construct(prv):
    kprv = [prv]
    S = prv
    for k in range(lv):
        T = [0] * n
        for i in range(n):
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
    for k in range(lv + 1):
        if dd & 1:
            v = kprv[k][v]
        dd >>= 1

    # assert depth[u] == depth[v]
    if u == v:
        return u

    for k in range(lv - 1, -1, -1):
        pu = kprv[k][u]
        pv = kprv[k][v]
        if pu != pv:
            u = pu
            v = pv

    # assert kprv[0][u] == kprv[0][v]
    return kprv[0][u]


def distance(u, v, kprv, depth):
    return depth[u] + depth[v] - 2 * depth[lca(u, v, kprv, depth)]


n, q = map(int, input().split())
m = [[] for _ in [0] * n]  # 近傍
for _ in [0] * (n - 1):
    a, b = map(int, input().split())
    m[a - 1] += [b - 1]
    m[b - 1] += [a - 1]
depth = [0] * n
prv = [-1] * n  # 親
c = [[] for _ in [0] * n]  # 子供
prv[0] = (1 << 63)  # 根が 0
l = [0]  # 根が 0
order = [0] * n  # 深さ優先探索での順番
o = 0
while l:
    v = l.pop()
    order[v] = o
    o += 1
    for u in m[v]:
        if prv[u] < 0:
            prv[u] = v
            c[v] += [u]
            depth[u] = depth[v] + 1
            l += [u]
prv[0] = None
lv = (n - 1).bit_length()
kprv = construct(prv)
for _ in range(q):
    u, v = map(int, input().split())
    if distance(u - 1, v - 1, kprv, depth) % 2:
        print('Road')
    else:
        print('Town')
