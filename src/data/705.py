from collections import deque

N, Q = map(int, input().split())

graph = [[] for _ in range(N)]
ans = []

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def bfs(u):
    queue = deque([u])
    d = [None] * (N)
    d[u] = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if d[i] is not None:
                continue
            d[i] = d[v] + 1
            queue.append(i)
    return d


dis, colors = bfs(0), [""] * N
for i in range(N):
    if dis[i] % 2 == 0:
        colors[i] = "red"
    else:
        colors[i] = "blue"

for _ in range(Q):
    c, d = map(int, input().split())
    color1, color2 = colors[c - 1], colors[d - 1]
    if color1 == color2:
        ans.append("Town")
    else:
        ans.append("Road")

print(*ans, sep="\n")
