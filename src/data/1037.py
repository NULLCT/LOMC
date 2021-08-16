import sys
from collections import deque, defaultdict

N, Q = map(int, input().split())

edges = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

INF = float("inf")
dist = {}
dist[0] = 0
visited = set()

q = deque()
q.append((0, 0))
while q:
    city, d = q.popleft()
    if city in visited:
        continue
    visited.add(city)

    for n_city in edges[city]:
        if n_city in visited:
            continue

        dist[n_city] = d + 1
        q.append((n_city, d + 1))

# print(dist)
for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1

    dx = abs(dist[c] - dist[d])
    # print(c, d, dx)
    if dx % 2 == 0:
        print("Town")
    else:
        print("Road")
