import sys

input = sys.stdin.readline
from collections import deque

N, Q = map(int, input().split())
graph = [[] for i in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
CD = []
for i in range(Q):
    a, b = map(int, input().split())
    CD.append([a, b])

visited = [0 for i in range(N + 1)]
G = [[], []]


def bfs(u):
    queue = deque([u])
    d = [None] * N  # uからの距離の初期化
    d[u] = 0  # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if d[i] is None:
                d[i] = d[v] + 1

                queue.append(i)
    return d


Ki = bfs(1)
for i in range(Q):
    c = CD[i][0]
    d = CD[i][1]

    if (Ki[c - 1] + Ki[d - 1]) % 2 == 1:
        print("Road")
    else:
        print("Town")
