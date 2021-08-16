import sys

input = sys.stdin.readline
from array import array
from collections import deque


def shortest_path_bfs(es: "隣接リスト", start: "始点"):
    INF = 1_000_000_000
    V = len(es)
    d = [INF] * V  # 頂点startからの最短距離
    que = deque()
    que.append(start)
    d[start] = 0
    while que:
        v = que.popleft()
        for e in es[v]:
            if d[e] == INF:
                d[e] = d[v] + 1
                que.append(e)

    return d


n, q = map(int, input().split())
es = [array("i") for _ in range(n)]
for i in range(n - 1):
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    es[start].append(end)
    es[end].append(start)

dist = shortest_path_bfs(es, 0)

res = [""] * q
for i in range(q):
    c, d = map(int, input().split())
    k = dist[c - 1] - dist[d - 1]
    res[i] = "Road" if k % 2 else "Town"

print(*res, sep="\n")
