import sys

input = sys.stdin.buffer.readline
inputs = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**6)
# '.'=46,'#'=35,'\n'=10
N, Q = map(int, input().split())

edges = [[] for i in range(1 + N)]
for i in range(N - 1):
    """#weighted->erase_,__,___=map(int,input().split())
    edges[_].append((__,___))
    edges[__].append((_,___))
    """
    _, __ = map(int, input().split())
    _ -= 1
    __ -= 1

    edges[_].append(__)
    edges[__].append(_)
    """
"""  #weighted->erase
LEVEL = [0] * (N + 1)
G = [[] for i in range(N + 1)]


def dfs(now, par=-1, c=0):
    LEVEL[now] = c
    for to in edges[now]:
        if to != par:
            G[now].append(to)
            dfs(to, now, c + 1)


dfs(0)

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


def dist(x, y):
    return LEVEL[x] + LEVEL[y] - 2 * LEVEL[query(x, y)]


for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    print("Town") if dist(c, d) % 2 == 0 else print("Road")
