import sys
import math
from collections import deque, Counter

sys.setrecursionlimit(10**7)
int1 = lambda x: int(x) - 1

mi = lambda: map(int, input().split())
li = lambda: list(mi())
mi1 = lambda: map(int1, input().split())
li1 = lambda: list(mi1())
mis = lambda: map(str, input().split())
lis = lambda: list(mis())

from collections import defaultdict
"""
d=defaultdict(int) #初期値 0
d=defaultdict(lambda:1) #初期値 1
"""

mod = 10**9 + 7
Mod = 998244353
INF = 10**18
ans = 0

# N: 頂点数
N, q = mi()
# edge:辺
edge = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
# Euler Tour の構築
S = []
F = [0] * N
depth = [-1] * N
depth[0] = 0


def dfs(v, d):
    F[v] = len(S)
    depth[v] = d
    S.append(v)
    for w in edge[v]:
        if depth[w] == -1:
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


#クエリ処理 0-index に注意
for i in range(q):
    c, d = mi1()
    t = query(c, d)
    s = depth[c] + depth[d] - 2 * depth[t]
    if s % 2 == 0:
        print('Town')
    else:
        print('Road')
