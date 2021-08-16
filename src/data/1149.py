n, q = map(int, input().split())
g = [[] for _ in range(0, n + 1)]

for i in range(0, n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

from collections import deque


def bfs(N: int, X: int, g):
    q = deque([X])
    visit = [float("inf") for _ in range(0, N)]
    visit[X] = 0

    while q:
        x = q.popleft()
        for dest in g[x]:
            if visit[dest] > visit[x] + 1:
                visit[dest] = visit[x] + 1
                q.append(dest)
    return visit


dist = bfs(n + 1, 1, g)
# print(dist)

anss = []
for i in range(0, q):
    c, d = map(int, input().split())
    if abs(dist[d] - dist[c]) % 2 == 0:
        anss.append("Town")
    else:
        anss.append("Road")

print("\n".join(anss))
