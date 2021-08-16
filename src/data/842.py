import sys

input = sys.stdin.readline

n, q = map(int, input().split())
g = [[] for _ in range(n)]  # 隣接リスト

for _ in range(n - 1):
    a, b = [int(x) for x in input().split()]
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

from collections import deque


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
# d = bfs(0)
# print(d)

ans = []
D_o = bfs(0)
for i in range(len(D_o)):
    if D_o[i] % 2 == 0:
        D_o[i] = 2
    else:
        D_o[i] = 1

for i in range(q):
    c, d = map(int, input().split())
    if D_o[c - 1] % 2 == 0:
        if D_o[d - 1] == 2:
            ans.append('Town')
        else:
            ans.append('Road')
    else:
        if D_o[d - 1] == 2:
            ans.append('Road')
        else:
            ans.append('Town')

for i in range(q):
    print(ans[i])
