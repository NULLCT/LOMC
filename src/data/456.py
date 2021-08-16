from collections import deque

n, m = map(int, input().split())
graph = [list() for _ in range(n)]

for _ in range(n - 1):
    u, k = [int(x) for x in input().split()]  # uは頂点番号、kは隣接頂点の個数
    u, k = u - 1, k - 1
    graph[u].append(k)
    graph[k].append(u)  # 無向グラフ

dist = [-1] * n  #距離
dist[0] = 0  #startは0

q = deque()
q.append(0)  #startは0
while q:  #qが空になるまで
    v = q.popleft()
    for x in graph[v]:
        if dist[x] != -1:  #更新
            continue
        dist[x] = 1 - dist[v]
        q.append(x)

for i in range(m):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if dist[c] != dist[d]:
        print("Road")
    else:
        print("Town")
