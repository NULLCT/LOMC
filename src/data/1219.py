n, qc = map(int, input().split())
edge = [[] for _ in range(n)]
for i in range(n - 1):
    x, y = map(int, input().split())
    edge[x - 1].append(y - 1)
    edge[y - 1].append(x - 1)
q, dist = [0], [-1] * n
dist[0] = 0
while q:
    node = q.pop()
    for e in edge[node]:
        if dist[e] == -1:
            dist[e] = dist[node] + 1
            q.append(e)
for _ in range(qc):
    c, d = map(int, input().split())
    if dist[c - 1] % 2 == dist[d - 1] % 2:
        print('Town')
    else:
        print('Road')
