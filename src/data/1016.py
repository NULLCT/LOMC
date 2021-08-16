N, Q = map(int, input().split())

from collections import deque

graph = []
for i in range(N):
    row = []
    graph.append(row)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

visited = []
for i in range(N):
    visited.append(False)

q = deque()
q.append(0)

visited[0] = True
dist = [0] * N
while len(q) > 0:
    i = q.popleft()
    for j in graph[i]:
        if not visited[j]:
            visited[j] = True
            q.append(j)
            dist[j] = dist[i] + 1
maxi = dist.index(max(dist))

visited = []
for i in range(N):
    visited.append(False)

q2 = deque()
q2.append(maxi)

visited[maxi] = True
dist = [0] * N
while len(q2) > 0:
    i = q2.popleft()
    for j in graph[i]:
        if not visited[j]:
            visited[j] = True
            q2.append(j)
            dist[j] = dist[i] + 1

for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    dai = max(dist[c], dist[d])
    sho = min(dist[c], dist[d])
    if (dai - sho) % 2 == 0:
        print("Town")
    else:
        print("Road")
