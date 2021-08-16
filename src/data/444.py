from collections import deque
import collections

N, Q = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

dist = [-1] * N
que = deque()
que.append(0)
dist[0] = 0
while que:
    now = que.popleft()
    for i in edges[now]:
        if dist[i] != -1:
            continue
        dist[i] = dist[now] + 1
        que.append(i)

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[c] + dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
