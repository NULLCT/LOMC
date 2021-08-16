#D
from collections import deque

N, Q = map(int, input().split())
edges = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

dist = [-1] * N


def bfs(x):
    que = deque([x])
    dist[x] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in edges[v]:
            if dist[w] > -1:
                continue
            dist[w] = d + 1
            que.append(w)


bfs(0)
#print(dist)
for i in range(Q):
    c, d = map(int, input().split())
    if (dist[d - 1] - dist[c - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
