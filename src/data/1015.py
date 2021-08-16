#!/usr/bin/env python3
import sys
from collections import defaultdict, deque

INF = float('inf')
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**7)


def db(*arg):
    print(*arg)


def div_ceil(x, y):
    return -(-x // y)


N, Q = map(int, readline().split())
ad_ls = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, readline().split())
    a, b = a - 1, b - 1
    ad_ls[a].append(b)
    ad_ls[b].append(a)

G = [[] for _ in range(N)]

dist = [0] * N
q = deque()
q.append((0, 0))
done = set([0])
while q:
    now, c = q.popleft()
    for nex in ad_ls[now]:
        if nex in done:
            continue
        dist[nex] = c + 1
        G[now].append(nex)
        done.add(nex)
        q.append((nex, c + 1))

S = []
F = [0] * N
depth = [0] * N
done = set()


def dfs(v, d):
    F[v] = len(S)
    depth[v] = d
    S.append(v)
    for w in G[v]:
        if w in done:
            continue
        dfs(w, d + 1)
        S.append(v)
        done.add(w)


dfs(0, 0)

INF = (N, None)

M = 2 * N
M0 = 2**(M - 1).bit_length()
data = [INF] * (2 * M0)
for i, v in enumerate(S):
    data[M0 - 1 + i] = (depth[v], i)
for i in range(M0 - 2, -1, -1):
    data[i] = min(data[2 * i + 1], data[2 * i + 2])


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


for _ in range(Q):
    c, d = map(int, readline().split())
    lca = query(c - 1, d - 1)
    d = dist[c - 1] + dist[d - 1] - 2 * dist[lca]
    # db('=====')
    # print(d)
    # print('lca', dist[lca])
    print('Town' if d % 2 == 0 else 'Road')
