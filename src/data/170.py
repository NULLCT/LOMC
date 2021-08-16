from collections import deque

N, Q = map(int, input().split())

G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

depth = [None for i in range(N)]

q = deque()
q.append(0)
depth[0] = 0

while q:
    v = q.popleft()
    for u in G[v]:
        if depth[u] is not None:
            continue
        depth[u] = depth[v] + 1
        q.append(u)

for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if depth[c] % 2 == depth[d] % 2:
        print('Town')
    else:
        print('Road')
