from collections import deque


def bfs(dist):
    queue = deque()
    queue.append(0)
    while queue:
        v1 = queue.popleft()
        for v2 in adj[v1]:
            if dist[v2] != -1:
                continue
            dist[v2] = dist[v1] + 1
            queue.append(v2)


N, Q = map(int, input().split())
adj = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    adj[a].append(b)
    adj[b].append(a)

dist = [-1] * N
dist[0] = 0

ans = bfs(dist)

# print(dist)

for _ in range(Q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    dis = abs(dist[c] - dist[d])
    if dis % 2:
        print("Road")
    else:
        print("Town")
