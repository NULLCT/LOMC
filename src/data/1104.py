from collections import deque
import sys

sys.setrecursionlimit(10000000)

N, Q = map(int, input().split())
a, b = [
    list(map((-1).__add__, i))
    for i in zip(*[list(map(int,
                            input().split())) for _ in range(N - 1)])
]
c, d = [
    list(map((-1).__add__, i))
    for i in zip(*[list(map(int,
                            input().split())) for _ in range(Q)])
]

to = [[] for _ in range(N)]
for i in range(N - 1):
    to[a[i]].append(b[i])
    to[b[i]].append(a[i])

stack = deque()
stack.append(0)

use = [False] * N
use[0] = True

G = [[] for _ in range(N)]

while stack:
    u = stack.pop()
    for v in to[u]:
        if use[v]:
            continue
        G[u].append(v)
        stack.append(v)
        use[v] = True

# N: 頂点数
# G[v]: 頂点vの子頂点 (親頂点は含まない)

# Euler Tour の構築
S = []
F = [0] * N
depth = [0] * N


def dfs(v, d):
    F[v] = len(S)
    depth[v] = d
    S.append(v)
    for w in G[v]:
        dfs(w, d + 1)
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


for i in range(Q):
    k = query(c[i], d[i])
    dist = depth[c[i]] + depth[d[i]] - 2 * depth[k]
    if dist % 2 == 0:
        print('Town')
    else:
        print('Road')
