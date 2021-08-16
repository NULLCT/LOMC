from collections import deque

n, Q = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
query = []
for _ in range(Q):
    c, d = map(int, input().split())
    query.append((c - 1, d - 1))
dist = [-1] * n
dist[0] = 0
q = deque([0])
while q:
    node = q.popleft()
    for c_node in graph[node]:
        if dist[c_node] >= 0:
            continue
        dist[c_node] = dist[node] + 1
        q.append(c_node)
for c, d in query:
    if (dist[c] + dist[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
