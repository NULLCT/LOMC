from collections import deque

n, Q = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

dist = [-1] * n
dist[0] = 0

q = deque()
q.append(0)

while q:
    v = q.popleft()
    for i in set(graph[v]):
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        q.append(i)

for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if abs(dist[c] - dist[d]) % 2 == 1:
        print("Road")
    else:
        print("Town")
