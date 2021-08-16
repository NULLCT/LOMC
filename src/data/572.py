n, q = map(int, input().split())

G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)

from collections import deque


def bfs(p):
    res = []
    used = [False] * (n)
    dq = deque([[p, 0]])
    while dq:
        v, i = dq.popleft()
        if used[v]: continue
        used[v] = True
        res.append([v, i])
        for u in G[v]:
            dq.append([u, i + 1])
    return res


P = bfs(0)
P.sort()

for _ in range(q):
    c, d = map(lambda x: int(x) - 1, input().split())
    if (P[c][1] + P[d][1]) % 2: print('Road')
    else: print('Town')
