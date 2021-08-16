N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
d = [None] * N
d[0] = 0
queue = [0]
l = 0
while l < len(queue):
    u = queue[l]
    l += 1
    for v in G[u]:
        if d[v] is None:
            d[v] = d[u] + 1
            queue.append(v)
for _ in range(Q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    print('Town' if (d[u] + d[v]) % 2 == 0 else 'Road')
