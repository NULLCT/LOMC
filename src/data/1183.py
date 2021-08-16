INF = 1 << 30

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    G[a].append(b)
    G[b].append(a)

dist = [INF] * N
dist[0] = 0

# DFS
stack = [0]
seen = [False] * N
while stack:
    v = stack.pop()
    seen[v] = True
    for next_v in G[v]:
        if seen[next_v]:
            continue
        dist[next_v] = min(dist[next_v], dist[v] + 1)
        stack.append(next_v)

for _ in range(Q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
    if (dist[c] + dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
