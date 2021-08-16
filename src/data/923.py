N, Q = map(int, input().split())

AB = [list(map(int, input().split())) for _ in range(N - 1)]
CD = [list(map(int, input().split())) for _ in range(Q)]

from collections import deque
import sys

sys.setrecursionlimit(100000000)

con = [deque() for _ in range(N)]
G = [deque() for _ in range(N)]
for a, b in AB:
    a, b = a - 1, b - 1
    con[a].append(b)
    con[b].append(a)

q = deque([0])
flag = [False] * N
while len(q) != 0:
    x = q.pop()
    if flag[x]:
        continue
    else:
        flag[x] = True
        for i in con[x]:
            if flag[i]:
                continue
            else:
                G[x].append(i)
                q.append(i)

# N: 頂点数
# G[v]: 頂点vの子頂点 (親頂点は含まない)

# Euler Tour の構築
S = deque([])
F = [0] * N
depth = [0] * N
flag = [False] * N


def dfs(v, d):
    F[v] = len(S)
    depth[v] = d
    S.append(v)
    flag[v] = True
    for w in G[v]:
        if flag[w]:
            continue
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


for c, d in CD:
    c, d = c - 1, d - 1
    x = depth[c] + depth[d] - 2 * query(c, d)
    if x % 2 == 0:
        print('Town')
    else:
        print('Road')
