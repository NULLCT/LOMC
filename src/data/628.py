"""
n = int(input())
a = list(map(int, input().split()))
xy = list(map(int, input().split()))
xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]
i, j = map(int, input().split())
"""
from collections import deque

n, q = map(int, input().split())
road = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    road[a - 1].append(b - 1)
    road[b - 1].append(a - 1)


def bfs(graph):
    dist = [-1] * n
    que = deque([0])
    dist[0] = 0
    while que:
        v = que.popleft()
        # v = que.pop()
        d = dist[v]
        for w in graph[v]:
            if dist[w] > -1:
                continue
            dist[w] = d + 1
            que.append(w)

    return dist


color = bfs(road)

for i in range(q):
    s_taka, s_aoki = map(int, input().split())

    if color[s_aoki - 1] % 2 == color[s_taka - 1] % 2:
        print('Town')
    else:
        print('Road')
