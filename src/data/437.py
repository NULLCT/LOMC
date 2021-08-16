from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify
from bisect import bisect_left, bisect_right
import sys, math, itertools, pprint, fractions

sys.setrecursionlimit(10**8)
mod = 10**9 + 7
INF = float('inf')


def inp():
    return int(sys.stdin.readline())


def inpl():
    return list(map(int, sys.stdin.readline().split()))


def inpl_1():
    return list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))


def err(x):
    print(x)
    exit()


LV = 20


def construct(prv):
    kprv = [prv]
    S = prv
    for k in range(20):
        T = [-1] * n
        for i in range(n):
            if S[i] == -1:
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


n, Q = inpl()
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = inpl_1()
    g[a].append(b)
    g[b].append(a)
pa = [-1] * n
dist = [0] * n
seen = [0] * n
seen[0] = 1
q = deque([0])
while q:
    u = q.popleft()
    for v in g[u]:
        if seen[v]: continue
        pa[v] = u
        dist[v] = dist[u] + 1
        q.append(v)
        seen[v] = 1

# pa[v] ->vの親ノード
#kprv[k][v] -> vから2^k回上に遡った時の頂点
kprv = construct(pa)
#dist[v] -> ルートからの深さ
#l -> a,bのLCA
for _ in range(Q):
    a, b = inpl_1()
    l = lca(a, b, kprv, dist)
    ln = dist[a] - dist[l] + dist[b] - dist[l]
    print('Town' if ln % 2 == 0 else 'Road')
