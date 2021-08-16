n, q = map(int, input().split())

G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)

from collections import deque

P = [-1] * n
P[0] = 0
dq = deque([0])
while dq:
    v = dq.popleft()
    for u in G[v]:
        if P[u] >= 0: continue
        P[u] = P[v] + 1
        dq.append(u)

for _ in range(q):
    c, d = map(lambda x: int(x) - 1, input().split())
    print('Road' if (P[c] + P[d]) % 2 else 'Town')
