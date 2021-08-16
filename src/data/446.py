import sys

N, Q = map(int, input().split())  # nは頂点の数、mは辺の数
g = [[] for _ in range(N)]  # 隣接リスト

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
from collections import deque


def bfs(u):
    queue = deque([u])
    d = [None] * N  # uからの距離の初期化
    d[u] = 0  #oad") 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d


T = bfs(0)
for i in range(N):
    if T[i] % 2 == 0:
        T[i] = 1
    else:
        T[i] = 0
#print(T)
for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if T[d] % 2 == T[c] % 2:
        print("Town")
    else:
        print("Road")
