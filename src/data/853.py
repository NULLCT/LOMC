from collections import deque

N, Q = map(int, input().split())

graph = [[] for _ in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

dist = [-1] * (N)
dist[0] = 0
que = deque()
que.append(0)
while que:
    v = que.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        que.append(i)
for _ in range(Q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if (dist[c] + dist[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
