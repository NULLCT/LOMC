from heapq import heappush, heappop

N, Q = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    edges[a - 1] += [b - 1]
    edges[b - 1] += [a - 1]

# 根 0 から BFS して, 0からの距離を図る
dist = [float("inf")] * N
dist[0] = 0

confirm = [False] * N  # 頂点までの距離が確定しているか
# hq は [頂点kまでの最短距離, 頂点k] を要素に持つ
# ヒープキューのソートキーにするため、最短距離が第一変数
hq = [(0, 0)]
# ダイクストラ法
while hq:
    d, v = heappop(hq)
    if confirm[v]:
        continue
    confirm[v] = True
    for w in edges[v]:
        if not confirm[w] and d + 1 < dist[w]:
            dist[w] = d + 1
            heappush(hq, (dist[w], w))

for q in range(Q):
    c, d = map(int, input().split())
    if (dist[c - 1] - dist[d - 1]) % 2:
        print("Road")
    else:
        print("Town")
