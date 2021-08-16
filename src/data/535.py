n, q = map(int, input().split())

G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)

from collections import deque

P = [0] * n
used = [False] * n
dq = deque([0])
while dq:
    v = dq.popleft()
    if used[v]: continue
    used[v] = True
    for u in G[v]:
        P[u] = P[v] + 1
        dq.append(u)

for _ in range(q):
    c, d = map(lambda x: int(x) - 1, input().split())
    if (P[c] + P[d]) % 2: print('Road')
    else: print('Town')
