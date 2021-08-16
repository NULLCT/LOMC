#n = int(input())
n, q = map(int, input().split())
#c = list(map(int, input().split()))
#l = [list(map(int, input().split())) for l in range(n)]
import sys

input = sys.stdin.readline

#n, m = map(int, input().split()) # nは頂点の数、mは辺の数
g = [[] for _ in range(n)]  # 隣接リスト

for _ in range(n - 1):
    a, b = [int(x) for x in input().split()]
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

from collections import deque


def bfs(u):
    queue = deque([u])
    d = [-1] * n  # uからの距離の初期化
    d[u] = 0  # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] == -1:
                d[i] = d[v] + 1
                queue.append(i)
    return d


# 0からの各頂点の距離
d = bfs(0)
#print(d)

for i in range(q):
    c, e = map(int, input().split())
    if (d[e - 1] - d[c - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
