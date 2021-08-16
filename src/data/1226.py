N, Q = list(map(int, input().split()))

edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    edges[a].append(b)
    edges[b].append(a)

stack = [1]
dist = [-1] * (N + 1)
dist[1] = 0
while stack:
    v = stack.pop()
    for nv in edges[v]:
        if dist[nv] == -1:
            dist[nv] = dist[v] + 1
            stack.append(nv)

for _ in range(Q):
    c, d = list(map(int, input().split()))
    if (dist[c] + dist[d]) % 2:
        print("Road")
    else:
        print("Town")
