import sys
from collections import deque

input = sys.stdin.readline

n, q = [int(x) for x in input().split()]  # nは頂点の数、mは辺の数
g = [[] for _ in range(n)]  # 隣接リスト
m = n - 1

for _ in range(m):
    a, b = [int(x) - 1 for x in input().split()]
    g[a].append(b)
    g[b].append(a)


def bfs(u):
    queue = deque([u])
    d = [None] * n  # uからの距離の初期化
    d[u] = 0  # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d


# 0からの各頂点の距離
queri = bfs(0)
for i in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    dd = queri[a] - queri[b]
    if dd % 2 == 1:
        print("Road")
    else:
        print("Town")
