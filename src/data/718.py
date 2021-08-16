from collections import deque

n, q = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (n + 1)

que = deque()

que.append(1)
dist[1] = 0

while que:
    u = que.popleft()

    for j in graph[u]:
        if dist[j] == -1:
            dist[j] = dist[u] + 1
            que.append(j)

for j in range(q):
    c, d = map(int, input().split())

    if abs(dist[c] - dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
