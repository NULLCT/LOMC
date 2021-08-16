n, q = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n - 1)]
cd = [list(map(int, input().split())) for _ in range(q)]

from collections import defaultdict

g = defaultdict(list)
for a, b in ab:
    g[a] += [b]
    g[b] += [a]


# Euler Tour
def dfs(u, d):
    # first visit
    vis = [-1] * (n + 1)
    # euler tour
    et = []
    que = [(u, d)]

    while len(que) > 0:
        u, d = que.pop()
        if u > 0:
            # 行きがけの処理
            vis[u] = len(et)
            et += [(u, d)]
            for v in g[u]:
                if vis[v] == -1:  # 未探索のみ
                    que += [(-v, d + 1)]  # 帰り
                    que += [(v, d + 1)]  # 行き
        else:
            # 帰りがけの処理
            et += [(u, d)]

    return vis, et


vis, et = dfs(1, 0)

t = [t for e, t in et]


def init_min(init_min_val):
    #set_val
    for i in range(n):
        seg_min[i + num_min - 1] = init_min_val[i]
    #built
    for i in range(num_min - 2, -1, -1):
        seg_min[i] = min(seg_min[2 * i + 1], seg_min[2 * i + 2])


def query_min(p, q):
    if q <= p:
        return ide_ele_min
    p += num_min - 1
    q += num_min - 2
    res = ide_ele_min
    while q - p > 1:
        if p & 1 == 0:
            res = min(res, seg_min[p])
        if q & 1 == 1:
            res = min(res, seg_min[q])
            q -= 1
        p = p // 2
        q = (q - 1) // 2
    if p == q:
        res = min(res, seg_min[p])
    else:
        res = min(min(res, seg_min[p]), seg_min[q])
    return res


n = len(t)
ide_ele_min = 10**5 + 1

#num_min:n以上の最小の2のべき乗
num_min = 2**(n - 1).bit_length()
seg_min = [ide_ele_min] * 2 * num_min

#init
init_min(t)

for c, d in cd:
    pc, pd = vis[c], vis[d]
    dc, dd = t[pc], t[pd]
    m = query_min(pc, pd)
    dist = dc + dd - 2 * m

    if dist % 2 == 0:
        print("Town")
    else:
        print("Road")
