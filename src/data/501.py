n, q = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(n - 1)]
cd = [list(map(int, input().split())) for _ in range(q)]

from collections import defaultdict

g = defaultdict(list)
for a, b in ab:
    g[a] += [b]
    g[b] += [a]

# Euler Tour の構築


def dfs(u, d):
    F = [0] * (n + 1)
    ET = []
    que = [(1, u, d)]

    while len(que) > 0:
        s, u, d = que.pop()
        #print(s, u, d)
        if s == 1:
            F[u] = len(ET)
            ET += [d]
            for v in g[u]:
                if F[v] == 0:
                    que += [(0, v, d + 1)]
                    que += [(1, v, d + 1)]
        else:
            ET += [d]

    return F, ET


F, ET = dfs(1, 0)


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


n = len(ET)
ide_ele_min = 10**5 + 1

#num_min:n以上の最小の2のべき乗
num_min = 2**(n - 1).bit_length()
seg_min = [ide_ele_min] * 2 * num_min

#init
init_min(ET)

for c, d in cd:
    pc, pd = F[c], F[d]
    dc, dd = ET[pc], ET[pd]
    m = query_min(pc, pd)
    #print(c,d,pc,pd,dc,dd,m)
    dist = dc + dd - 2 * m
    #print(dist, sd[pc:pd+1])
    if dist % 2 == 0:
        print(  #dist, 
            "Town")
    else:
        print(  #dist, 
            "Road")
