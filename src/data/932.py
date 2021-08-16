from collections import deque

n, q = list(map(int, input().split()))
graph = [[] * n for i in range(n)]
for i in range(n - 1):
    ai, bi = list(map(int, input().split()))
    graph[ai - 1].append(bi - 1)
    graph[bi - 1].append(ai - 1)

INF = float("inf")
dist = [INF for i in range(n)]
dist[0] = 0
seen = [False] * n
que = deque([(0, 0)])
while que:
    node, d = que.popleft()
    if seen[node]:
        continue
    seen[node] = True
    for ne in graph[node]:
        dist[ne] = d + 1
        que.append((ne, d + 1))

for qi in range(q):
    ci, di = list(map(int, input().split()))
    if (dist[ci - 1] + dist[di - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
