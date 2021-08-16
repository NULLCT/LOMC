n, Q = map(int, input().split())

dist = [-1] * (n + 1)
g = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

q = [1]
dist[1] = 0
while q:
    now = q.pop()
    for next in g[now]:
        if dist[next] == -1:
            q.append(next)
            dist[next] = dist[now] + 1

for _ in range(Q):
    c, d = map(int, input().split())
    if (dist[c] + dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
