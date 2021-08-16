n, q = map(int, input().split())
l = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    l[a].append(b)
    l[b].append(a)

que = [0]
dist = [None] * n
dist[0] = 0

for v in que:
    for vv in l[v]:
        if dist[vv] is None:
            dist[vv] = dist[v] + 1
            que.append(vv)

for _ in range(q):
    c, d = map(int, input().split())
    if (dist[c - 1] - dist[d - 1]) % 2 == 0:
        print('Town')
    else:
        print('Road')
