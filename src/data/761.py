N, Q = map(int, input().split())
path = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    path[a - 1].append(b - 1)
    path[b - 1].append(a - 1)
seen = [False] * N
dist = [0] * N
nxt = [0]
depth = 1
while len(nxt) > 0:
    v = nxt.pop()
    for u in path[v]:
        if not seen[u]:
            dist[u] = dist[v] + 1
            nxt.append(u)
    seen[v] = True
cd = [list(map(int, input().split())) for i in range(Q)]
for q in cd:
    if (dist[q[0] - 1] + dist[q[1] - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
