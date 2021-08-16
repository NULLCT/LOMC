import sys

input = sys.stdin.readline

N, Q = [int(x) for x in input().split()]  # nは頂点の数、mは辺の数
g = [[] for _ in range(N)]  # 隣接リスト

for _ in range(N - 1):
    a, b = [int(x) for x in input().split()]
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

from collections import deque


def bfs(u):
    queue = deque([u])
    d = [None] * N  # uからの距離の初期化
    d[u] = 0  # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d


A = bfs(0)
for _ in range(Q):
    c, d = [int(x) for x in input().split()]
    num = A[c - 1] - A[d - 1]
    if num % 2 == 0:
        print("Town")
    else:
        print("Road")
