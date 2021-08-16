mod = 10**9 + 7
import collections

n, q = map(int, input().split())

edges = [[] for _ in range(n)]
queue = collections.deque([0])
visited = [True for _ in range(n)]
dist = [0 for i in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append(b)
    edges[b].append(a)

while queue:
    now = queue.popleft()
    visited[now] = False
    for ed in edges[now]:
        if visited[ed]:
            queue.append(ed)
            dist[ed] = (dist[now] + 1) % 2

for _ in range(q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if dist[c] == dist[d]:
        print('Town')
    else:
        print('Road')
