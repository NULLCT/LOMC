from sys import setrecursionlimit

setrecursionlimit(10**6)

n, q = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a] += [b]
    g[b] += [a]

# n: 頂点数
# G[v]: 頂点vの子頂点 (親頂点は含まない)

# Euler Tour の構築
S = []
F = [0] * n
depth = [0] * n


def dfs(v, d):
    F[v] = len(S)
    depth[v] = d
    S.append(v)
    for w in g[v]:
        if depth[w] == 0:
            dfs(w, d + 1)
            S.append(v)


dfs(0, 0)

# 存在しない範囲は深さが他よりも大きくなるようにする
InF = (n, None)

# LCAを計算するクエリの前計算
M = 2 * n
M0 = 2**(M - 1).bit_length()
data = [InF] * (2 * M0)
for i, v in enumerate(S):
    data[M0 - 1 + i] = (depth[v], i)
for i in range(M0 - 2, -1, -1):
    data[i] = min(data[2 * i + 1], data[2 * i + 2])


# LCAの計算 (generatorで最小値を求める)
def _query(a, b):
    yield InF
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
    ans = depth[c] + depth[d] - 2 * depth[query(c, d)]
    if ans % 2 == 1:
        print("Road")
    else:
        print("Town")
