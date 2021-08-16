from collections import deque
import sys

sys.setrecursionlimit(10**7)

n, q = map(int, input().split())
G = [set() for i in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    G[a - 1].add(b - 1)
    G[b - 1].add(a - 1)


def dfs0(i, par=-1):
    for to in G[i]:
        if to == par: continue
        if i in G[to]:
            G[to].remove(i)
        dfs0(to, i)


# dfs0(i, -1)

# N: 頂点数
# G[v]: 頂点vの子頂点 (親頂点は含まない)
N = n
# Euler Tour の構築
S = []
F = [0] * N
depth = [0] * N


def dfs(v, d, par=-1):
    F[v] = len(S)
    depth[v] = d
    S.append(v)
    for w in G[v]:
        if w == par: continue
        dfs(w, d + 1, v)
        S.append(v)


dfs(0, 0)

# 存在しない範囲は深さが他よりも大きくなるようにする
INF = (N, None)

# LCAを計算するクエリの前計算
M = 2 * N
M0 = 2**(M - 1).bit_length()
data = [INF] * (2 * M0)
for i, v in enumerate(S):
    data[M0 - 1 + i] = (depth[v], i)
for i in range(M0 - 2, -1, -1):
    data[i] = min(data[2 * i + 1], data[2 * i + 2])


# LCAの計算 (generatorで最小値を求める)
def _query(a, b):
    yield INF
    a += M0
    b += M0
    while a < b:
        if b & 1:
            b -= 1
            yield data[b - 1]
        if a & 1:
            yield data[a - 1]
            a += 1
        a >>= 1
        b >>= 1


# LCAの計算 (外から呼び出す関数)
def query(u, v):
    fu = F[u]
    fv = F[v]
    if fu > fv:
        fu, fv = fv, fu
    return S[min(_query(fu, fv + 1))[1]]


for i in range(q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    p = query(c, d)
    dist = depth[c] + depth[d] - 2 * depth[c]
    if dist % 2 == 0:
        print('Town')
    else:
        print('Road')
