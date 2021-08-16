from collections import deque

N, Q = map(int, input().split())
E = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    E[a - 1].append(b - 1)
    E[b - 1].append(a - 1)

dist = [0] * N
d = deque()
d.append(0)
while d:
    v = d.popleft()
    for i in E[v]:
        if dist[i] != 0: continue
        dist[i] = dist[v] + 1
        d.append(i)

for _ in range(Q):
    c, d = map(int, input().split())

    even = bool(dist[c - 1] % 2) ^ bool(dist[d - 1] % 2)
    print('Road' if even else 'Town')
