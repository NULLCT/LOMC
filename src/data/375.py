from collections import deque

n, q = map(int, input().split())
G = [[] for i in range(n)]  # n : Number of vertices
for i in range(n - 1):  # n - 1 : Number of edges
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)  # Undirected graph

dist = [None] * n  # Distance to each vertex
que = deque([0])
dist[0] = 0
color = [None] * n
color[0] = True
while que:
    v = que.popleft()
    d = dist[v]
    for w in G[v]:
        if dist[w] is not None:
            continue
        dist[w] = d + 1
        if (dist[w] % 2 == 0):
            color[w] = True
        else:
            color[w] = False
        que.append(w)

for i in range(q):
    s, t = map(int, input().split())
    if (color[s - 1] == color[t - 1]):
        print("Town")
    else:
        print("Road")
