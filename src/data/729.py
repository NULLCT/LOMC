n, q = map(int, input().split())
dist = [0 for i in range(n + 1)]

adj = [[] for i in range(n + 1)]
par = [0 for i in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())

    adj[a].append(b)
    adj[b].append(a)


def bfs(root):
    q = [root]
    vis = [False for _ in range(n + 1)]
    vis[1] = True

    while q:
        now = q.pop(0)

        for nxt in adj[now]:
            if vis[nxt] == False:
                q.append(nxt)
                dist[nxt] = dist[now] + 1
                vis[now] = True


def find_p(node):
    k = dist[node]
    for can in range(adj[node]):
        if dist[can] < k:
            par[node] = can


bfs(1)

for _ in range(q):
    a, b = map(int, input().split())

    if (dist[a] + dist[b]) % 2 == 0:
        print('Town')
    else:
        print('Road')
