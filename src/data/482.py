import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n, q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n - 1)]
cd = [list(map(int, input().split())) for _ in range(q)]
ki = [[] for _ in range(n)]
for a, b in ab:
    a, b = a - 1, b - 1
    ki[a].append(b)
    ki[b].append(a)

# n: 頂点数
# ki: 木
# Euler Tour の構築
S = []  # Euler Tour
F = [0] * n  # F[v]:vにはじめて訪れるステップ
depth = [0] * n  # 0を根としたときの深さ


def dfs(v, pare, d):
    F[v] = len(S)
    depth[v] = d
    S.append(v)
    for w in ki[v]:
        if w == pare: continue
        dfs(w, v, d + 1)
        S.append(v)


dfs(0, -1, 0)
ary = [[depth[v], v] for v in range(n)]

# Sをセグメント木に乗せる
# u,vのLCAを求める:S[F[u]:F[v]+1]のなかでdepthが最小の頂点を探せば良い
# F[u]:uに初めてたどるつくステップ
# S[F[u]:F[v]+1]:はじめてuにたどり着いてつぎにvにたどるつくまでに訪れる頂点
# 存在しない範囲は深さが他よりも大きくなるようにする
INF = (n, None)
# LCAを計算するクエリの前計算
M = 2 * n
M0 = 2**(M - 1).bit_length()  # M以上で最小の2のべき乗
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


for c, d in cd:
    c, d = c - 1, d - 1
    lca = query(c, d)
    tmp = depth[c] + depth[d] - depth[lca] * 2
    if tmp % 2 == 0:
        print("Town")
    else:
        print("Road")
