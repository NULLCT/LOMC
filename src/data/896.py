from collections import deque

N, Q = map(int, input().split())
a = [None] * N
b = [None] * N
# g = [[False for _ in range(N)] for _ in range(N)]
g = [[] for _ in range(N)]

for n in range(N - 1):
    a[n], b[n] = map(int, input().split())
    g[a[n] - 1].append(b[n] - 1)
    g[b[n] - 1].append(a[n] - 1)


def bfs(s):
    dist = [None] * N
    que = deque([s])
    dist[s] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in g[v]:
            if dist[w] is not None:
                continue
            dist[w] = d + 1
            que.append(w)
    return dist.index(d), dist


_, dist = bfs(0)

for q in range(Q):
    c, d = map(int, input().split())
    print('Road' if (dist[c - 1] + dist[d - 1]) % 2 == 1 else 'Town')
