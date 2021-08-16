import collections

N, Q = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)
q = collections.deque()
q.append(0)
dist = [-1] * N
dist[0] = 0
while len(q) != 0:
    v = q.popleft()
    d = dist[v]
    for w in graph[v]:
        if dist[w] > -1:
            continue
        dist[w] = d + 1
        q.append(w)
for i in range(Q):
    c, d = map(int, input().split())
    if (dist[c - 1] + dist[d - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
