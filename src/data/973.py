def dfs(u):
    s = []
    s.append(u)
    while s:
        u = s.pop()
        visited[u] = 1
        for v in adj[u]:
            if not visited[v]:
                d[v] = d[u] + 1
                s.append(v)


N, Q = map(int, input().split())
adj = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

d = [-1] * N
visited = [0] * N
d[0] = 0
dfs(0)

for i in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if (d[x] + d[y]) % 2 == 0:
        print("Town")
    else:
        print("Road")
