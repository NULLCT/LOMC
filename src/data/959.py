import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N, Q = map(int, input().split())
D = [[] for i in range(N)]
G = [[] for i in range(N)]
S = []
F = [0] * N
for i in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    D[u].append(v)
    D[v].append(u)
#根が決められておらず、Dでとりあえず双方向を記録し、Gで方向を決めている
depth = [-1] * N
import sys

sys.setrecursionlimit(10**9)
from collections import deque

d = deque()
d.append((0, 0))
e = deque()
de = 1
while d:
    now, pre = d.popleft()
    for nex in D[now]:
        if nex != pre:
            G[now].append(nex)
            e.append((nex, now))
    d = e
#print(G)

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


def query(u, v):
    fu = F[u]
    fv = F[v]
    if fu > fv:
        fu, fv = fv, fu
    return S[min(_query(fu, fv + 1))[1]]


for q in range(Q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    a = query(u, v)
    r = depth[u] - depth[a] + depth[v] - depth[a]
    if r % 2 == 0:
        print('Town')
    else:
        print('Road')
