from collections import deque

N, Q = map(int, input().split())

a, b = [0] * (N - 1), [0] * (N - 1)
for i in range(N - 1):
    a[i], b[i] = map(int, input().split())

c, d = [0] * Q, [0] * Q
for i in range(Q):
    c[i], d[i] = map(int, input().split())

graph = [[] for _ in range(N)]
for i in range(N - 1):
    graph[a[i] - 1].append(b[i] - 1)
    graph[b[i] - 1].append(a[i] - 1)

dist = [-1 for _ in range(N)]
dist[0] = 0

que = deque()
que.append(0)

while que:
    current_node = que.popleft()
    for near_node in graph[current_node]:
        if dist[near_node] != -1:
            continue
        dist[near_node] = dist[current_node] + 1
        que.append(near_node)

for i in range(Q):
    if (dist[c[i] - 1] + dist[d[i] - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
